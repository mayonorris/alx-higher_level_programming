#!/usr/bin/python3
"""Module - square
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square
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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square
        Returns:
            tuple: Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square
        Args:
            value (tuple): Position value to set
        Raises:
            TypeError: If position is not a tuple of two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square
        Returns:
            int: Area of the square
        """
        return (self.size ** 2)

    def my_print(self):
        """Print the square using '#' character
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
