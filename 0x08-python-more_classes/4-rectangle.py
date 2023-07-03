#!/usr/bin/python3
"""
Module 2-rectangle
Contains class Rectangle with private attribute width and height,
and public area and perimeter methods
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """Class Constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @property
    def height(self):
        """Getter returns height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter funtion for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter function for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return width * height"""
        areaRectangle = self.__width * self.__height
        return areaRectangle

    def perimeter(self):
        """Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeterRectangle = 2 * (self.__width + self.__height)
            return perimeterRectangle

    def __str__(self) -> str:
        """str formated output"""
        if self.__height == 0 or self.__width == 0:
            return ""
        pic = "\n".join(["#" * self.__width for i in range(self.__height)])
        return pic

    def __repr__(self) -> repr:
        """repr formated output to oval()"""
        return "Rectangle(width={}, height={})".format(self.__width, self.__height)
