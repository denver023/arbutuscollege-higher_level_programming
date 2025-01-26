#!/usr/bin/python3
"""
Module 4-inherits_from
Contains a function inherits_from that checks if an object is an instance of
a class.
"""

def inherits_from(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
