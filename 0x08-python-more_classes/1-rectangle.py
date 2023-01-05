#!/usr/bin/python3

"""
Class Rectangle which actually defines a rectangle
"""


class Rectangle:
    """
    Class Rectangles which creates a rectangle with attributes
    """

    def __init__(self, width=0, height=0):
        """ Method that initializes the rectangle

        Args:
            width: The width of the rectangle
            height: The width of the rectangle


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the value of the width of the rectangle

        Returns:
            The width of the rectangle


        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be of integral value")
        if value < 0:
            raise ValueError("Width must be greater than or equal to 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the height of the rectangle

        Returns:
            The height of the rectangle


        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be of integral value")
        if value < 0:
            raise ValueError("Height must be greater than or equal to 0")
        self.__height = value
