#!/usr/bin/python3

"""
Class that defines a rectangle
"""


class Rectangle:
    """Defines the class Rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the Rectangle

        Args:
            width: The width of the Rectangle
            height: The height of the Rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Method that returns the value of the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width of the rectangle

        Return:
            No Returns

        Raises:
            TypeError: If the width is not an integer
            ValueError: If teh width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the value of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height of the rectangle

        Return:
        No Return

        Raises:
           TypeError: If width is not an integer
            ValueError: If the width is less than the zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

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

        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Method that returns the string character representation of
        the Rectangle"""

        rectangle = " "

        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            rectangle += ("#" * self.__width) + "\n"

        return rectangle[:-1]
