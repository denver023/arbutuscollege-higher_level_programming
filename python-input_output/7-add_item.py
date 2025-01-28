#!/usr/bin/python3
"""
This script adds all arguments passed to it via the command line
to a list stored in a JSON file named 'add_item.json'.
If the file does not exist, it will be created.
Each time the script is run, the arguments are appended to the list.
"""
import sys
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file

def add_items():
    try:
        # Try loading the existing list from the file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        items = []
    
    # Add command-line arguments to the list
    items.extend(sys.argv[1:])
    
    # Save the updated list back to the JSON file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_items()
