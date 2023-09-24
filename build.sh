#!/usr/bin/env bash
# exit on error
set -o errexit

# Install libraries
pip install -r requirements.txt

# Apply DB changes
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python iLabAPI/manage.py createsuperuser --no-input
fi