#!/usr/bin/python3
"""
Module 0-lookup
Contains a function `lookup` that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.

    Returns:
        List of strings representing the object's attributes and methods.
    """
    return dir(obj)
