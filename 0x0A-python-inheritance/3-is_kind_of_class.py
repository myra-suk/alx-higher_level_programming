#!/usr/bin/python3

"""Defines if the object is of the same class or is inherited from"""


def is_kind_of_class(obj, a_class):
    """ Function taht returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True: if obj is an instance of a_class
        False: othehrwise
    """
    return isinstance(obj, a_class)
