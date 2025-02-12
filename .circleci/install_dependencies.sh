#!/usr/bin/env bash
# This script installs the dependencies to download and validate all studies

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install python dependencies
pip install -r requirements.txt

# Install and configure Git LFS
echo "Installing Git LFS..."
cd ~/
wget https://github.com/git-lfs/git-lfs/releases/download/v2.3.4/git-lfs-linux-amd64-2.3.4.tar.gz
tar -xvf git-lfs-linux-amd64-2.3.4.tar.gz
cd git-lfs-2.3.4
sudo ./install.sh
cd ~/repo
sudo chown -R circleci .git
git lfs install --skip-smudge
rm -rf git-lfs-linux-amd64-2.3.4.tar.gz git-lfs-2.3.4

# Clone cBioPortal core
cd ~/
git clone --depth 1 -b main https://github.com/cBioPortal/cbioportal-core.git

# Make test reports location
cd ~/
mkdir ~/test-reports
mkdir ~/test-reports/ERRORS
