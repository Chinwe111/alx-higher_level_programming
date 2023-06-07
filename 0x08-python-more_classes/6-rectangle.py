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
        ...
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        else:
            if height < 0:
                raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """
        ...
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        ...
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        ...
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += "#" * self.__width
            output += "\n"

        return output.rstrip()

    def __repr__(self):
        """
        Return the string representation of the retangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message for every deletion of a rectangle
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
