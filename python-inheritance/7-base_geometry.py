#!/usr/bin/python3
# 7_base_geometry.py
# Defines BaseGeometry class with area() and integer_validator() methods.

class BaseGeometry:
    """
    BaseGeometry class for geometric shapes with area and value validation methods.
    """

    def area(self):
        """
        Raises an exception to indicate that the method is not implemented.

        Example:
            >>> bg = BaseGeometry()
            >>> bg.area()
            Traceback (most recent call last):
                ...
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is a positive integer.

        Args:
            name (str): Variable name.
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("age", 25)
            >>> bg.integer_validator("age", "hello")
            Traceback (most recent call last):
                ...
            TypeError: age must be an integer
            >>> bg.integer_validator("age", -1)
            Traceback (most recent call last):
                ...
            ValueError: age must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
