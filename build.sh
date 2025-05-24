#!/bin/bash
set -o errexit

# Debug: Print environment
echo "🔍 Python version:"
python --version
echo "🔍 Pip version:"
pip --version

# Debug: Show working directory
echo "📍 Current directory: $(pwd)"
echo "📝 Directory contents:"
ls -la

# Install dependencies
echo "🔧 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create SQLite database directory if it doesn't exist
echo "📁 Setting up database directory..."
mkdir -p backend/db

# Move to Django directory
echo "📂 Moving to Django project directory..."
cd backend

# Debug: Verify Django files
echo "📍 Django directory: $(pwd)"
echo "📝 Django directory contents:"
ls -la

# Django commands
echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "🔄 Running migrations..."
python manage.py migrate --noinput

echo "✅ Build completed successfully!"