#!/usr/bin/python3
"""This module defines a class MyList that inherits from list"""


class MyList(list):
    """MyList class that prints the list sorted"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
