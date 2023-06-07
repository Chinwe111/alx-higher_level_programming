#!/usr/bin/python3
"""Defines the class Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle"""
        if type(width) is not int:
            raise TypeError("Width must be an integer")
        else:
            if width < 0:
                raise ValueError("Width must be >= 0")
        if type(height) is not int:
            raise TypeError("Height must be an integer")
        else:
            if height < 0:
                raise ValueError("Height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        else:
            if width < 0:
                raise ValueError("Width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        else:
            if height < 0:
                raise ValueError("Height must be >= 0")
        self.__height = value
