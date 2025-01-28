#!/usr/bin/python3
"""
This module provides a function to read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
