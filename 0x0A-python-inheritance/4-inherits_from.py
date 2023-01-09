#!/usr/bin/python3

"""Defines whether an object has inherited the instance directly or indirectly
   from a class"""


def inherits_from(obj, a_class):
    """Defines if an object is inherited directly or indirectly

    Args:
        objs: object
        a_class: class type

    Returns:
        True: if obj is an instance of a_class
        False: otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
