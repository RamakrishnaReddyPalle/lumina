#!/usr/bin/env bash

set -e

echo "Installing Lumina..."

python scripts/check_dependencies.py

pip install -r requirements.txt

python scripts/install_desktop.py

python scripts/install_service.py

echo
echo "Lumina Installed"
echo