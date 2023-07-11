#!/usr/bin/python3

"""
Module 2-append_write.py

contains a function that appends a string at the end of a text
"""


def append_write(filename="", text=""):
    """A function appends a string at end of a text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
