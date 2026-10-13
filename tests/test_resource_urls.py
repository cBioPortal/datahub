"""Offline tests: no external servers, study downloads, or extra packages."""

from contextlib import redirect_stderr, redirect_stdout
import http.client
import importlib.util
import io
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import Mock, patch


SCRIPT = Path(__file__).resolve().parents[1] / '.circleci' / 'validate_resource_urls.py'
SPEC = importlib.util.spec_from_file_location('resource_urls', SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.dns = patch.object(validator.socket, 'getaddrinfo', return_value=[
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('93.184.216.34', 443))
        ]).start()
        self.addCleanup(patch.stopall)
        # If any test escapes its simulated connection, fail before opening a socket.
        self.socket = patch.object(validator.socket, 'create_connection',
                                   side_effect=AssertionError('Unexpected network access')).start()

    def response(self, status, location=None):
        response = Mock(status=status)
        response.getheader.return_value = location
        return response

    def test_200_uses_get_and_closes_without_reading_body(self):
        response = self.response(200)
        with patch.object(validator, 'PublicConnection') as factory:
            connection = factory.return_value
            connection.getresponse.return_value = response
            self.assertIsNone(validator.check_url('https://example.org/file?x=1#fragment'))
        factory.assert_called_once_with('example.org', 443, '93.184.216.34', True, 10)
        args, kwargs = connection.request.call_args
        self.assertEqual(('GET', '/file?x=1'), args)
        self.assertEqual('identity', kwargs['headers']['Accept-Encoding'])
        response.read.assert_not_called()
        response.close.assert_called_once()
        connection.close.assert_called_once()

    def test_non_200_statuses_fail(self):
        for status in (201, 204, 403, 404, 429, 500):
            with self.subTest(status=status), patch.object(validator, 'PublicConnection') as factory:
                factory.return_value.getresponse.return_value = self.response(status)
                self.assertIn('HTTP {}'.format(status), validator.check_url('https://example.org'))

    def test_public_redirect_rechecks_destination(self):
        first, second = Mock(), Mock()
        first.getresponse.return_value = self.response(302, 'https://other.example/file')
        second.getresponse.return_value = self.response(200)
        with patch.object(validator, 'PublicConnection', side_effect=[first, second]) as factory:
            self.assertIsNone(validator.check_url('https://example.org'))
        self.assertEqual(2, self.dns.call_count)
        self.assertEqual('other.example', factory.call_args_list[1].args[0])
        first.close.assert_called_once()
        second.close.assert_called_once()

    def test_relative_redirect(self):
        with patch.object(validator, 'PublicConnection') as factory:
            factory.return_value.getresponse.side_effect = [
                self.response(301, '/new'), self.response(200)]
            self.assertIsNone(validator.check_url('https://example.org/old'))
            self.assertEqual('/new', factory.return_value.request.call_args.args[1])

    def test_redirect_to_private_address_is_never_contacted(self):
        with patch.object(validator, 'PublicConnection') as factory:
            factory.return_value.getresponse.return_value = self.response(302, 'http://169.254.169.254/')
            self.assertIsNotNone(validator.check_url('http://example.org'))
            factory.assert_called_once()

    def test_unsafe_urls_never_open_a_connection(self):
        urls = ['', 'na', 'file:///etc/passwd', 'ftp://example.org/file',
                'https://user:secret@example.org', 'http://localhost',
                'http://localhost.', 'http://x.localhost', 'http://127.0.0.1',
                'http://10.1.2.3', 'http://169.254.169.254', 'http://[::1]',
                'http://[::ffff:127.0.0.1]', 'http://224.0.0.1',
                'http://[64:ff9b::7f00:1]', 'https://example.org:22',
                'https://example.org:0', 'https://example.org:bad',
                'https://example.org/\r\nX-Test: injected']
        with patch.object(validator, 'PublicConnection') as factory:
            for url in urls:
                with self.subTest(url=url):
                    self.assertIsNotNone(validator.check_url(url))
            factory.assert_not_called()

    def test_mixed_public_and_private_dns_is_rejected(self):
        self.dns.return_value.append((socket.AF_INET, socket.SOCK_STREAM, 6, '', ('10.0.0.1', 443)))
        with patch.object(validator, 'PublicConnection') as factory:
            self.assertIsNotNone(validator.check_url('https://example.org'))
            factory.assert_not_called()

    def test_dns_failure_and_empty_answers_fail(self):
        with patch.object(validator, 'PublicConnection') as factory:
            self.dns.return_value = []
            self.assertIsNotNone(validator.check_url('https://example.org'))
            self.dns.side_effect = socket.gaierror('cannot resolve secret.example')
            error = validator.check_url('https://secret.example?token=secret')
            self.assertIn('gaierror', error)
            self.assertNotIn('secret', error)
            factory.assert_not_called()

    def test_missing_location_and_redirect_limit_fail(self):
        with patch.object(validator, 'PublicConnection') as factory:
            factory.return_value.getresponse.return_value = self.response(302)
            self.assertIn('no Location', validator.check_url('https://example.org'))
            factory.return_value.getresponse.return_value = self.response(302, '/loop')
            self.assertIn('Too many redirects', validator.check_url('https://example.org'))

    def test_https_downgrade_fails(self):
        with patch.object(validator, 'PublicConnection') as factory:
            factory.return_value.getresponse.return_value = self.response(302, 'http://example.org')
            self.assertIn('downgrades', validator.check_url('https://example.org'))
            factory.assert_called_once()

    def test_timeout_and_bad_headers_close_connection_and_redact_values(self):
        for exception in (TimeoutError('secret'), http.client.BadStatusLine('secret')):
            with self.subTest(exception=exception), patch.object(validator, 'PublicConnection') as factory:
                factory.return_value.getresponse.side_effect = exception
                error = validator.check_url('https://example.org?token=secret')
                self.assertIn(type(exception).__name__, error)
                self.assertNotIn('secret', error)
                factory.return_value.close.assert_called_once()

    def test_connection_pins_checked_address_and_preserves_tls_hostname(self):
        raw_socket = Mock()
        self.socket.side_effect = None
        self.socket.return_value = raw_socket
        with patch.object(validator.ssl, 'create_default_context') as context:
            connection = validator.PublicConnection('example.org', 443, '93.184.216.34', True, 10)
            connection.connect()
            self.socket.assert_called_once_with(('93.184.216.34', 443), 10)
            context.return_value.wrap_socket.assert_called_once_with(raw_socket, server_hostname='example.org')
            self.dns.assert_not_called()  # The connect step cannot resolve the name again.
            connection.close()

    def test_tls_failure_closes_raw_socket(self):
        self.socket.side_effect = None
        raw_socket = self.socket.return_value
        with patch.object(validator.ssl, 'create_default_context') as context:
            context.return_value.wrap_socket.side_effect = OSError('TLS failed')
            connection = validator.PublicConnection('example.org', 443, '93.184.216.34', True, 10)
            with self.assertRaises(OSError):
                connection.connect()
            raw_socket.close.assert_called_once()

    def test_real_http_parser_reads_headers_only(self):
        class HeaderStream(io.BytesIO):
            def close(self):
                self.position_at_close = self.tell()
                super().close()

        headers = b'HTTP/1.1 200 OK\r\nContent-Length: 1000000000\r\n\r\n'
        stream = HeaderStream(headers + b'BODY MUST NOT BE READ')
        self.socket.side_effect = None
        self.socket.return_value.makefile.return_value = stream
        self.assertIsNone(validator.check_url('http://example.org/file'))
        self.assertEqual(len(headers), stream.position_at_close)
        self.socket.return_value.close.assert_called_once()
        self.assertIn(b'Host: example.org', self.socket.return_value.sendall.call_args.args[0])

    def test_redirect_cannot_add_credentials(self):
        with patch.object(validator, 'PublicConnection') as factory:
            factory.return_value.getresponse.return_value = self.response(
                302, 'https://user:secret@other.example/file')
            error = validator.check_url('https://example.org')
            self.assertIn('credentials', error)
            self.assertNotIn('secret', error)
            factory.assert_called_once()

    def test_unicode_path_and_idna_hostname(self):
        with patch.object(validator, 'PublicConnection') as factory:
            factory.return_value.getresponse.return_value = self.response(200)
            self.assertIsNone(validator.check_url('https://\u00e9xample.org/\u00e9?q=\u00e9'))
            self.assertEqual('xn--xample-9ua.org', factory.call_args.args[0])
            self.assertEqual('/%C3%A9?q=%C3%A9', factory.return_value.request.call_args.args[1])


class FileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.study = self.root / 'public' / 'study'
        self.study.mkdir(parents=True)
        self.check = patch.object(validator, 'check_url', return_value=None).start()
        self.addCleanup(patch.stopall)
        patch.object(validator.socket, 'create_connection',
                     side_effect=AssertionError('Unexpected network access')).start()

    def write(self, name, content):
        path = self.study / name
        path.write_text(content, encoding='utf-8')
        return path

    def run_main(self, *studies):
        output, errors = io.StringIO(), io.StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            status = validator.main(['--root-directory', str(self.root)] + list(studies or ['public/study']))
        return status, output.getvalue(), errors.getvalue()

    def test_comments_bom_blank_lines_reordered_headers_and_cache(self):
        path = self.write('data_resource_sample.txt', '\ufeff# comment\n\nURL\tRESOURCE_ID\nhttps://example.org\tR1\nhttps://example.org\tR2\n')
        self.assertEqual([], validator.validate_resource_file(path, {}))
        self.check.assert_called_once_with('https://example.org')

    def test_error_has_physical_line_number_and_never_echoes_url(self):
        self.check.return_value = 'HTTP 404 (expected 200)'
        path = self.write('data_resource_patient.txt', '# comment\n\nRESOURCE_ID\tURL\nR1\thttps://example.org?token=secret\n')
        errors = validator.validate_resource_file(path, {})
        self.assertIn(':4: HTTP 404', errors[0])
        self.assertNotIn('secret', errors[0])

    def test_definitions_without_urls_are_skipped(self):
        path = self.write('data_resource_definition.txt', 'RESOURCE_ID\tRESOURCE_TYPE\tDISPLAY_NAME\nR1\tSTUDY\tReport\n')
        self.assertEqual([], validator.validate_resource_file(path, {}))
        self.check.assert_not_called()

    def test_missing_url_header_duplicate_header_and_empty_file_fail(self):
        for content in ('RESOURCE_ID\nR1\n', 'URL\tURL\nx\tx\n', ''):
            with self.subTest(content=content):
                path = self.write('data_resource_study.txt', content)
                self.assertTrue(validator.validate_resource_file(path, {}))
        self.check.assert_not_called()

    def test_lfs_pointer_does_not_silently_pass(self):
        path = self.write('data_resource_patient.txt', validator.LFS_HEADER + '\noid sha256:abc\nsize 123\n')
        self.assertIn('Git LFS pointer', validator.validate_resource_file(path, {})[0])
        self.check.assert_not_called()

    def test_short_and_extra_rows_are_reported(self):
        path = self.write('data_resource_study.txt', 'RESOURCE_ID\tURL\nR1\nR2\turl\textra\n')
        self.assertEqual(2, len(validator.validate_resource_file(path, {})))
        self.check.assert_not_called()

    def test_unreadable_and_invalid_utf8_files_fail(self):
        path = self.study / 'data_resource_study.txt'
        self.assertIn('Cannot read', validator.validate_resource_file(path, {})[0])
        path.write_bytes(b'\xff')
        self.assertIn('Cannot read', validator.validate_resource_file(path, {})[0])

    def test_main_checks_selected_studies_and_excludes_archives(self):
        self.write('data_resource_study.txt', 'RESOURCE_ID\tURL\nR1\thttps://example.org\n')
        archive = self.study / 'archived_files'
        archive.mkdir()
        (archive / 'data_resource_study.txt').write_text('bad', encoding='utf-8')
        other = self.root / 'public' / 'other'
        other.mkdir()
        (other / 'data_resource_study.txt').write_text('bad', encoding='utf-8')
        status, output, errors = self.run_main('public/study', str(self.study))
        self.assertEqual(0, status)
        self.assertEqual('', errors)
        self.assertIn('0 error(s)', output)
        self.check.assert_called_once()

    def test_cache_is_shared_between_files_and_failures_set_exit_code(self):
        self.check.return_value = 'HTTP 500 (expected 200)'
        for kind in ('patient', 'sample', 'study'):
            self.write('data_resource_{}.txt'.format(kind), 'RESOURCE_ID\tURL\nR1\thttps://example.org\n')
        status, output, errors = self.run_main()
        self.assertEqual(1, status)
        self.assertEqual(3, errors.count('HTTP 500'))
        self.assertIn('3 error(s)', output)
        self.check.assert_called_once()

    def test_nonexistent_or_outside_study_directory_fails(self):
        for study in ('public/missing', '..'):
            with self.subTest(study=study):
                self.assertEqual(1, self.run_main(study)[0])
        self.check.assert_not_called()

    def test_no_resources_is_success(self):
        status, output, errors = self.run_main()
        self.assertEqual((0, ''), (status, errors))
        self.assertIn('0 resource file(s)', output)

    def test_resource_symlink_is_rejected(self):
        target = self.root / 'target.txt'
        target.write_text('RESOURCE_ID\tURL\nR1\thttps://example.org\n', encoding='utf-8')
        path = self.study / 'data_resource_study.txt'
        try:
            path.symlink_to(target)
        except OSError:
            self.skipTest('Creating symlinks is unavailable on this system')
        status, output, errors = self.run_main()
        self.assertEqual(1, status)
        self.assertIn('must stay inside', errors)
        self.check.assert_not_called()


if __name__ == '__main__':
    unittest.main()
