#!/usr/bin/python3

"""
Class that defines a rectangle
"""


class Rectangle:
    """Defines the class Rectangle

    Attributes:
    number_of_instances: The number of rectangle instances
    print_symbol: The symbol use for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that initializes the Rectangle

        Args:
            width: The width of the Rectangle
            height: The height of the Rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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
            raise ValueError("width must be >= 0")
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

        if self.__width == 0 or self.__height == 0:
            return 0

        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Method that returns the string character representation of
        the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return the string representatipon of the Rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Prints a message when the Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
