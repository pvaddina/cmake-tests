#!/bin/bash
set -e

# Print the path
pwd

# Set up Python virtual environment (optional)
source /opt/venv/bin/activate
echo "source /opt/venv/bin/activate" >> ~/.bashrc

# Verify the active Python environment (optional)
python --version
pip --version

# Install all the python modules defined in the requirements.txt
pip install -r .devcontainer/requirements.txt

# Conan configuration
conan profile detect --name=pvdefault
conan profile list

