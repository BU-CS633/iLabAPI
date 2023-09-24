#!/usr/bin/env bash
# exit on error
set -o errexit

# Install libraries
pip install -r requirements.txt

# Apply DB changes
python manage.py migrate