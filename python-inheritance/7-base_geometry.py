#!/usr/bin/python3
"""
Module 7-base_geometry
Contains the class BaseGeometry with methods area and integer_validator.
"""


class BaseGeometry:
    """
    A class BaseGeometry with methods area and integer_validator.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as a positive integer.

        Args:
            name: The name to be used in the exception message.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
