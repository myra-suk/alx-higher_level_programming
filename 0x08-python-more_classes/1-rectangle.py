#!/usr/bin/python3

"""
Class Rectangle which actually defines a rectangle
"""


class Rectangle:
    """
    Define the class Rectangle whih creates a Rectangle
    """

    def __init__(self, width=0, height=0):
        """ Method that initializes the Rectangle

        Args:
            width: The width of the Rectangle
            height: The width of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the value of the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Gets the attributes of the rectangle

        Returns:
            No returns

        Raises:
            TypeError: If the width is not an integer
            ValueError: If the value of the width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Gets the attributes of the rectangle

        Returns:
            No returns

        Raises:
            TypeError: If the height is not an integer
            ValueError: If the value of the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
