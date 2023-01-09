#!/usr/bin/python3

"""Defines a base geometry Class BaseGeometry"""


class BaseGeometry:
    """Class that represents Geometry"""

    def area(self):
        """Method that defines the area of a geometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that receives the value property

        Args:
            name: name of the object
            value: value of the property

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
