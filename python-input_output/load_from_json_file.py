#!/usr/bin/python3
"""
This module provides a function to create a Python object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Creates a Python object from a "JSON file".

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        object: The Python object represented by the JSON string in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
