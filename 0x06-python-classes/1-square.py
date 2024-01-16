#!/usr/bin/python3
"""Module - Square
This module contains a class Square that defines a square.
"""


class Square:
    """Class - Square
    Defines a square with a private instance attribute: size.
    """

    def __init__(self, size):
        """__init__ - Initializes a new instance of the Square class.
        Parameters:
          - size (int): The size of the square.
        """
        self.__size = size
