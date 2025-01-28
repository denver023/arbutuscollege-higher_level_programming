#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Try to load existing items from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with empty list
    items = []

# Add all arguments (excluding script name) to the list
items.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(items, filename)
