#!/usr/bin/python3
"""
This module provides a function to read and print the content of a text file.
"""
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout. This is a very long docstring that exceeds the 79-character limit and will cause an E501 error.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
