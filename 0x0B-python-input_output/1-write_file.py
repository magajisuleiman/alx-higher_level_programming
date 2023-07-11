#!/usr /bin/python3

"""
Module 1-write_file.py

contains a function that write a text and return the count
"""


def write_file(filename="", text=""):
    """A function that writes to text and count"""
    counter_text = 0
    with open(filename, "w", encoding="UTF8") as file:
        file.write(text)
        for i in text:
            counter_text += 1
    return counter_text
