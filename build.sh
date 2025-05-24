#!/bin/bash
set -o errexit

# Debug information
echo "🔍 Current environment:"
echo "Working directory: $(pwd)"
echo "Python version: $(python --version)"

# Create SQLite directories
echo "📁 Creating SQLite directories..."
mkdir -p backend/db
mkdir -p /opt/render/project/src/db

# Set permissions
echo "🔒 Setting database permissions..."
chmod 777 backend/db
chmod 777 /opt/render/project/src/db

# Install dependencies
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Django setup
echo "🚀 Setting up Django..."
cd backend
python manage.py collectstatic --noinput
python manage.py migrate --noinput

echo "✅ Build completed!"