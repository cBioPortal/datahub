# datahub audit / transformation scripts

Companion tooling for `datahub-behavioral-differences-v2.md`. All scripts run against
a checkout of cBioPortal datahub (`public/` studies); LFS files must be smudged first
(datahub's `.lfsconfig` sets `fetchexclude=*`, so pass `--exclude=""`):

```bash
git lfs pull --include="public/<study>/**" --exclude=""
```

## Scripts

| Script | Mode | Purpose |
|---|---|---|
| `scan_cna_oncotree.py` | read-only | quick scan: duplicate CNA gene rows (naive, same-file key only) + Oncotree drift; writes `~/scan_results.json` |
| `cna_merge.py` | writes (has `--check`) | fuse duplicate CNA rows exactly like the pipelines JAR (`CopyNumberAlterationUtilImpl`): merge when clean, first-row-wins fallback on conflict/parse error. Needs `--gene-table` / `--gene-alias` |
| `oncotree_audit.py` | read-only | full Oncotree drift report vs latest stable API: stale codes, CANCER_TYPE / CANCER_TYPE_DETAILED mismatches; writes `oncotree_audit.md` + `.json` |
| `oncotree_apply.py` | writes (has `--check`) | apply the JAR's `convertCancerTypesFromOncotree`: default = datahub path (only adds missing columns), `--force` = non-datahub overwrite behavior |
| `make_oncotree_doc.py` | read-only | render the compact `datahub-oncotree-audit.md` from `oncotree_audit.json` |
| `add_timeline_meta.py` | writes (has `--dry-run`) | write missing `meta_timeline*.txt` for bare `data_timeline*.txt` (section 2 of the doc; 30 meta files across 9 studies) |
| `add_supp_meta.py` | writes (has `--dry-run`) | write missing `meta_clinical_supp*.txt` for bare `data_clinical_supp*.txt`; datatype SAMPLE_ATTRIBUTES when header has SAMPLE_ID, else PATIENT_ATTRIBUTES (section 3; 24 meta files) |

## Data files

- `gene_table.tsv` / `gene_alias_table.tsv` — dumped 2026-08-19 from ClickHouse
  `cbioportal_public_blue.gene` / `.gene_alias` (44,896 genes, 58,171 aliases).
  Refresh via the hermes-gateway container:

```bash
docker exec hermes-gateway sh -c 'clickhouse-client --config-file /opt/data/.config/clickhouse/clickhouse_client_config_public.yaml -q "SELECT entrez_gene_id, hugo_gene_symbol FROM cbioportal_public_blue.gene FORMAT TSV"' > gene_table.tsv
docker exec hermes-gateway sh -c 'clickhouse-client --config-file /opt/data/.config/clickhouse/clickhouse_client_config_public.yaml -q "SELECT entrez_gene_id, gene_alias FROM cbioportal_public_blue.gene_alias FORMAT TSV"' > gene_alias_table.tsv
```

## Typical run

```bash
cd ~/Code/datahub/public
python3 cna_merge.py --gene-table gene_table.tsv --gene-alias gene_alias_table.tsv --check */data_cna*.txt
python3 oncotree_audit.py --root ~/Code/datahub/public
python3 oncotree_apply.py --check */data_clinical_sample.txt
```
