""" This module implements a linked list data structure using the Node class """



class Node:
    """ Node data structure """

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Linked_List:
    """ Double sided Linked List data structure """

    def __init__(self, head: Node = None):
        self.head = head
        self.tail = head

    def push_front(self, data):
        """ Adds item to head of list """
        if self.is_empty():
            self.head = self.tail = Node(val=data)
        node = Node(val=data, next=self.head)
        self.head = node

    def push_back(self, data):
        """ Adds item to tail of list """
        if self.is_empty():
            self.head = self.tail = Node(val=data)
        node = Node(val=data, next=None, prev=self.tail)
        self.tail = node

    def pop_front(self):
        """ Removes item from head of list """
        if self.is_empty():
            return None
        stored = self.head.val
        self.head = self.head.next
        return stored

    def pop_back(self):
        """ Removes item from tail of list """
        if self.is_empty():
            return None
        stored = self.tail.val
        self.tail = self.tail.prev
        return stored

    def extend_back(self, collection):
        pass
        # TODO: Implement making sure input is an iterable

    def extend_front(self, collection):
        pass
        # TODO: Implement making sure input is an iterable

    def is_empty(self) -> bool:
        """ Returns true if list is empty else false """
        return self.head is None and self.tail is None

    def print(self) -> bool:
        """ Visual representation of the linked list """


    # TODO: Implement an __iter__ method
    # TODO: Write Test Suite
    # TODO: Implement print
    # TODO: Implement equality
