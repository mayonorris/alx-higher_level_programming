#!/usr/bin/python3
"""Module - Node and SinglyLinkedList
"""


class Node:
    """Node class for a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Initialize a Node
        Args:
            data (int): Data for the node
            next_node (Node): Next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node
        Returns:
            int: Data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node
        Args:
            value (int): Data value to set
        Raises:
            TypeError: If data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the linked list
        Returns:
            Node: Next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list
        Args:
            value (Node): Next node to set
        Raises:
            TypeError: If next_node is not a Node or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class
    """
    def __init__(self):
        """Initialize a singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list
        Args:
            value (int): Data value for the new node
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Convert the linked list to a string
        Returns:
            str: String representation of the linked list
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return (result)
