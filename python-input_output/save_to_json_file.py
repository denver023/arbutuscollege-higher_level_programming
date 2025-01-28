#!/usr/bin/python3
"""
This module provides a function to save a Python object to a file using JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object to serialize to JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
