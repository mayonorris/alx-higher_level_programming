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
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area - Computes and returns the area of the square.
        """
        return (self.__size ** 2)
