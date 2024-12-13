#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
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
        self.__size = size
