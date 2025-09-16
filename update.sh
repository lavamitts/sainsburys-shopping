#!/bin/bash

# Exit on error
set -e

# Activate virtual environment
source .venv/bin/activate

# Get outdated packages
echo "Checking for outdated packages..."
uv pip list --outdated > outdated_packages.txt

# Initialize line counter
line_counter=0

# Loop through outdated packages and upgrade each
while IFS= read -r line; do
    line_counter=$((line_counter + 1))
    
    # Skip header lines (first two lines of the output)
    if [ "$line_counter" -le 2 ]; then
        continue
    fi

    # Extract package name from the line
    package=$(echo "$line" | awk '{print $1}')
    echo "Updating $package..."
    uv pip install --upgrade "$package"
done < outdated_packages.txt

# Clean up
rm outdated_packages.txt

# Export updated packages
uv pip freeze > requirements.txt

# Deactivate
deactivate

echo "All packages have been updated using uv."
