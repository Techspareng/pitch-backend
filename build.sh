#!/bin/bash
# Strict error handling
set -o errexit

# Debug information
echo "🔍 Current environment:"
echo "Working directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

# Install dependencies
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Prepare database directory
echo "🗄️ Setting up database..."
mkdir -p backend/db

# Django commands
echo "🚀 Configuring Django..."
cd backend
python manage.py collectstatic --noinput
python manage.py migrate --noinput

echo "✅ Build completed!"