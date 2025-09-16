#!/bin/bash

# Activate the virtual environment
source /Users/mattlavis/projects/personal-dev/shopping/venv/bin/activate

# Check if a date argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 YYYY-MM-DD"
    exit 1
fi

# The input date is now passed as the first argument
input_date="$1"

# Run the Python script with the date input
python /Users/mattlavis/projects/personal-dev/shopping/gen.py "$input_date"
