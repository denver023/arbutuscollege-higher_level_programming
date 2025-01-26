#!/usr/bin/python3
"""
Module 6-base_geometry
Contains the class BaseGeometry with a public instance method area.
"""


class BaseGeometry:
    """
    A class BaseGeometry with a method area that raises an exception.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
