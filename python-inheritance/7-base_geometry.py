#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base class for geometry objects"""

    def area(self):
        """Method to compute area

        Raises:
            Exception: This method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate integer value

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
