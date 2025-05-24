#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Show current directory
pwd
ls -la

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Navigate to Django project directory
cd backend

# Debug: Show Django directory contents
pwd
ls -la

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate