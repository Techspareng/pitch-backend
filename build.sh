#!/bin/bash
set -o errexit

echo "📍 Current directory: $(pwd)"
echo "📝 Directory contents:"
ls -la

echo "🔧 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📂 Moving to Django project directory..."
cd backend

echo "📍 Django directory: $(pwd)"
echo "📝 Django directory contents:"
ls -la

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input

echo "🔄 Running migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"