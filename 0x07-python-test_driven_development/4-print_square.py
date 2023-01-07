#!/usr/bin/python3

"""Defines a function that prints a square"""


def print_square(size):

    """
    Print a square with the # character

    Return:
        No return

    Raises:
        TypeError: If size is not an integer
        ValueErrot: If size is less than O
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
