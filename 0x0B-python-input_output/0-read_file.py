#!/usr/bin/python3

"""
Module 0-read_file.py
"""


def read_file(filename=""):
    """
    function that reads a text file and prints

    Argumet:
    filename
    """
    with open(filename, "r", encoding="UTF8") as file:
        for line in file:
            result = print(line.rstrip())
    return result
