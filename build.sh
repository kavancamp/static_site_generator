#!/bin/bash

set -e

# Navigate to the script's directory (project root)
cd "$(dirname "$0")"

echo "Building site into docs/ with base path: /static_site_generator/"
python3 src/main.py "/static_site_generator/"
echo "✅ Site built successfully into docs/"