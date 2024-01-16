#!/usr/bin/python3
"""Module - Square
This module contains a class Square that defines a square.
"""


class Square:
    """Class - Square
    Defines a square with a private instance attribute: size.
    """

    def __init__(self, size=0):
        """__init__ - Initializes a new instance of the Square class.
        Parameters:
          - size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """size - Getter method to retrieve the value of the size attribute.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """size - Setter method to set the value of the size attribute.
        Parameters:
          - value (int): The size value to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """area - Computes and returns the area of the square.
        """
        return (self.__size ** 2)
