#!/usr/bin/pyhton3

"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints tect with two new lines after each '.?:' character

    Return:
        No Return

    Raises:
        TypeError: If text is not of string value
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end=""))
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
