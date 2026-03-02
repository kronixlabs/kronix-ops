#!/usr/bin/env bash
set -euo pipefail

echo "Setting up kronix-ops..."

# Check Python version
python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
required="3.11"
if [[ "$(printf '%s\n' "$required" "$python_version" | sort -V | head -n1)" != "$required" ]]; then
  echo "Error: Python $required+ required (found $python_version)"
  exit 1
fi

# Create virtualenv if not present
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "Created virtual environment at .venv"
fi

source .venv/bin/activate

pip install --upgrade pip -q
pip install -r requirements.txt -q

# Ensure config exists
if [ ! -f "config/settings.yaml" ]; then
  cp config/settings.example.yaml config/settings.yaml
  echo "Created config/settings.yaml — fill in your credentials before running."
fi

echo "Setup complete. Activate with: source .venv/bin/activate"
