#!/usr/bin/python3
"""
Module 1-my_list
Contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of the built-in list class that adds a method
    to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
