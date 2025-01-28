#!/usr/bin/python3
"""
This module provides a function to append a string to the end of a text file in UTF-8 encoding.
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text string to append into the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
