#!/usr/bin/python3
"""
This module defines the Rectangle class, inheriting from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
