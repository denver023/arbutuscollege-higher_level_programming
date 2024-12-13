#!/usr/bin/python3
"""
This module defines a class Square that represents a square with private
attributes and methods for calculating the area and modifying its size.
"""

class Square:
    """
    A class that defines a square.

    Attributes:
    size (int): The size of the square.

    Methods:
    area(): Returns the area of the square.
    size: Property to get and set the size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

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
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
