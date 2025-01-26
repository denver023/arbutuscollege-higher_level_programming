#!/usr/bin/python3
# 7_base_geometry.py
# Defines the BaseGeometry class with methods for area calculation and value validation.

class BaseGeometry:
    """
    Base class for geometry shapes with area and value validation.
    """

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is a positive integer.

        Args:
            name (str): Variable name.
            value (int): Value to check.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
