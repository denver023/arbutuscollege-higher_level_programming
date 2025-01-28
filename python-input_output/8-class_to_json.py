#!/usr/bin/python3
"""Module that converts a class to JSON-serializable dictionary"""


def class_to_json(obj):
    """Returns dictionary description of object for JSON serialization

    Args:
        obj: Instance of a Class

    Returns:
        Dictionary description with simple data structure for JSON serialization
    """
    return obj.__dict__
