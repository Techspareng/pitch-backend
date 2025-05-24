#!/usr/bin/env bash
# exit on error
set -o errexit

# Debugging: Print current directory
pwd

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Navigate to Django project directory
cd backend

# Debugging: Print current directory after cd
pwd

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate