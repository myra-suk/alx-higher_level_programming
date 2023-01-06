#!/usr/bin/python3

"""
Class that defines a rectangle
"""


class Rectangle:
    """Defines the class Rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances
        print_symbol (any): The symbol used for string representation
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

    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area of the two

        Args:
            rect_1: The first instance of a rectangle
            rect_2: The second instance of a rectangle

         Raises:
            TypeError: If none of the instances are rectangles

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be instance of the class Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be instance of the class Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

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
