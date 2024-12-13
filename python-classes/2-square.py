#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size'.
It also includes validation for the 'size' attribute to ensure it is an integer
and greater than or equal to zero.
"""

class Square:
    """
    A class that represents a square.

    Attributes:
    size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new square with a given size.

        Args:
        size (int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it's a valid integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
