#!/usr/bin/python3


"""
A module that implements the a Linked List using

python classes
"""


class Node:
    """ A node class that defines the node of linked list """
    def __init__(self, data, next_node=None):
        """ Instantiate the class with data and next_node"""
        self.data = data
        self.next_node = next_node

    def get_data(self):

        """ A getter that retrieves the value of data """
        return self.__data

    def set_data(self, value):
        """ A setter that sets the value of data """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    def get_next_node(self):
        """ A getter that retrieved the value of the next node """
        return self.__next_node

    def set_next_node(self, value):
        """ A setter that sets the value of next node """
        if value is None or isinstance(value, self.__class__):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    data = property(get_data, set_data)
    next_node = property(get_next_node, set_next_node)


class SinglyLinkedList:
    """
    This class defines a singly linked list
    using the node class to create the list
    """
    def __init__(self):
        """Initializes the class with the private attr. head node as None"""
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new node into the Singly Linked list
        and also sorting the entries.. thus making sure the data in
        the linked list is sorted """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            ptr = self.__head
            initial_node = None
            while ptr is not None:
                if ptr.data >= new_node.data:
                    break
                initial_node = ptr
                ptr = ptr.next_node
            if initial_node is None:
                new_node.next_node = ptr
                self.__head = new_node
            else:
                initial_node.next_node = new_node
                new_node.next_node = ptr

    def __str__(self):
        """ A string representation of the whole data in the linked list """
        ptr = self.__head
        str_rep = ""
        while ptr is not None:
            str_rep += str(ptr.data) + "\n"
            ptr = ptr.next_node
        return str_rep[:-1]
