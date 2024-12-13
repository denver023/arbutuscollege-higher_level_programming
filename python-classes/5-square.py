#!/usr/bin/python3
"""
This module defines a class Square with attributes size and position,
including methods to calculate the area and print the square with the `#` character.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square (row, column).

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square using the `#` character, respecting its position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with optional size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): A tuple of two positive integers representing the position
                              of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the `#` character, respecting its position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
