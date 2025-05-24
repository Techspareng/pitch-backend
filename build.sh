#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📂 Moving to Django project directory..."
cd backend

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running migrations..."
python manage.py migrate
echo "✅ Build completed successfully!"
# Debugging: Print current directory after migration
pwd