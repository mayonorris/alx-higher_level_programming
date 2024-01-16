#!/usr/bin/python3
"""Module - Square class
"""


class Square:
    """Square class with private size attribute
    """
    def __init__(self, size=0):
        """Initialize a Square
        Args:
            size (number): Size of the square
        """
        self.size = size

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
            value (number): Size value to set
        Raises:
            TypeError: If size is not a number (float or integer)
            ValueError: If size is less than 0
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """Calculate the area of the square
        Returns:
            number: Area of the square
        """
        return (self.__size ** 2)

    def __eq__(self, other):

        """Check if two squares are equal based on area
        Args:
            other (Square): Another square to compare
        Returns:
            bool: True if areas are equal, False otherwise
        """
        return (self.area() == other.area())

    def __ne__(self, other):

        """Check if two squares are not equal based on area
        Args:
            other (Square): Another square to compare
        Returns:
            bool: True if areas are not equal, False otherwise
        """
        return (not self.__eq__(other))

    def __gt__(self, other):

        """Check if the area of the square is greater than the area of another square
        Args:
            other (Square): Another square to compare
        Returns:
            bool: True if area is greater, False otherwise
        """
        return (self.area() > other.area())

    def __ge__(self, other):

        """Check if the area of the square is greater than or equal to the area of another square
        Args:
            other (Square): Another square to compare
        Returns:
            bool: True if area is greater than or equal, False otherwise
        """
        return (self.area() >= other.area())

    def __lt__(self, other):

        """Check if the area of the square is less than the area of another square
        Args:
            other (Square): Another square to compare
        Returns:
            bool: True if area is less, False otherwise
        """
        return (self.area() < other.area())

    def __le__(self, other):

        """Check if the area of the square is less than or equal to the area of another square
        Args:
            other (Square): Another square to compare
        Returns:
            bool: True if area is less than or equal, False otherwise
        """
        return (self.area() <= other.area())
