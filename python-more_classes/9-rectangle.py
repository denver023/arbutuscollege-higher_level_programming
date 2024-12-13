#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height properties, tracks
the number of instances, allows custom print symbols, compares areas of rectangles,
and includes a class method to create a square.
"""

class Rectangle:
    """
    A Rectangle class with private width and height attributes and class
    attributes to track the number of instances and custom print symbols.
    
    Attributes:
        __width (int): Private width of the rectangle
        __height (int): Private height of the rectangle
        number_of_instances (int): Class attribute that tracks the number of
        Rectangle instances
        print_symbol (str): Class attribute that determines the symbol used
        for the string representation of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either width or
            height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        String representation of the rectangle, displaying the rectangle
        with the `print_symbol` characters.

        Returns:
            str: The rectangle as a string with `print_symbol` characters,
            or an empty string if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """
        String representation of the rectangle to recreate a new instance
        using eval().

        Returns:
            str: A string representation of the rectangle, e.g.,
            Rectangle(2, 4)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when the rectangle instance is deleted and decrement
        the number of instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles and returns the rectangle with the
        bigger or equal area.

        Args:
            rect_1 (Rectangle): First rectangle to compare
            rect_2 (Rectangle): Second rectangle to compare

        Returns:
            Rectangle: The rectangle with the larger area, or rect_1 if both
            rectangles have the same area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that returns a new Rectangle instance with width == height.

        Args:
            size (int, optional): The size of the square (width = height).
            Defaults to 0.

        Returns:
            Rectangle: A new rectangle instance with width == height == size.
        """
        return cls(size, size)
