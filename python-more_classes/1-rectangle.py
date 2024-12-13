#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height properties.
"""

class Rectangle:
    """
    A Rectangle class with private width and height attributes.
    
    Attributes:
        __width (int): Private width of the rectangle
        __height (int): Private height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the private width attribute.

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private width attribute with validation.

        Args:
            value (int): The width to set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        # Check if width is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        # Check if width is non-negative
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """
        Getter for the private height attribute.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private height attribute with validation.

        Args:
            value (int): The height to set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        # Check if height is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        # Check if height is non-negative
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
