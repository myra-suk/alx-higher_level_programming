#!/usr/bin/python3

"""Returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Function that returns the list of the availale attributes
       and methods of an object

    Args:
        obj: The instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
