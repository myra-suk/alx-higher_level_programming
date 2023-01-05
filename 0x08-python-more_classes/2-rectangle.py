#!/usr/bin/python3

"""
Class that defines a rectangle
"""


class Rectangle:
    """Define the class Rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the Rectangle

        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the value of the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width of the rectangle

        Returns:
            No Returns

        Raises:
            TypeError: If width is not an integer
            ValueError: If the width is less than the zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height of the rectangle

        Returns:
            No Returns

        Raises:
            TypeError: If the height is not an integer
            ValueError: If the height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height

    def area(self):
        """ Method that calulates the area of the Rectangle

        Returns:
            The area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Method that calulates the perimeter of the Rectangle

        Returns:
            The perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))
