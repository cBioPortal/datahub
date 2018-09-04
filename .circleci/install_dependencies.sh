sudo pip install -r requirements_py
wget https://github.com/git-lfs/git-lfs/releases/download/v2.3.4/git-lfs-linux-amd64-2.3.4.tar.gz
tar -xvf git-lfs-linux-amd64-2.3.4.tar.gz
cd git-lfs-2.3.4
sudo ./install.sh
cd ~/repo
sudo chown -R circleci .git
git lfs install --skip-smudge

git remote add upstream git@github.com:cbioportal/datahub.git
git clone --depth 1 -b master https://github.com/cbioportal/cbioportal.git
cd ~/repo/.circleci
# make test reports location:
mkdir ~/repo/test-reports
mkdir ~/repo/test-reports/ERRORS
