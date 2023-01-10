#!/usr/bin/python3

"""Returns the dictionary description with a siple data structure
for a JSON serialization of an object"""


def class_to_json(obj):
    """Function that retuns the dictionary description of an obj"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
