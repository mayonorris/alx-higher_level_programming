#!/usr/bin/python3
"""Module - Square class
"""


class Square:
    """Square class with private size and position attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square
        Args:
            size (int): Size of the square
            position (tuple): Position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square
        Returns:
            int: Size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value (int): Size value to set
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square
        Returns:
            tuple: Position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square
        Args:
            value (tuple): Position value to set
        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square
        Returns:
            int: Area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the character '#'
        """
        if self.__size == 0:
            print()
            return()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Convert the square to a string (same behavior as my_print())
        Returns:
            str: String representation of the square
        """
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return (result.strip())
