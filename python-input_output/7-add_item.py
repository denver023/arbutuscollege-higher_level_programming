#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing data if the file exists, otherwise start with an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
