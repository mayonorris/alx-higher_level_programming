#!/usr/bin/python3
"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle class with width, height attributes, area, and perimeter methods
    """

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method to calculate the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method to calculate the rectangle perimeter"""
        if (self.__width is 0 or self.__height is 0):
            return (0)
        return (self.__width *2 + self.__height * 2)
