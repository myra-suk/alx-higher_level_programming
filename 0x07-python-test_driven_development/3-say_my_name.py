#!/usr/bin/python3

"""Defines a funtion that prints the first name and last name"""


def say_my_name(first_name, last_name=""):
    """Prints a name

    Returns:
        No returns

    Raises:
        TypeError: If either first_name or last_name are not string values
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name ust be a string")
    print("My name is {} {}".format(first_name, last_name))
