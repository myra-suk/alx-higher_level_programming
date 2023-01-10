#!/usr/bin/python3

"""Defines a funtion that reads the contents of a file"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file as the output"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
