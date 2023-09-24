#!/usr/bin/env bash
# exit on error
set -o errexit

# Install libraries
pip install -r requirements.txt

# Fetch static files
python manage.py collectstatic --no-input

# Apply DB changes
python manage.py migrate