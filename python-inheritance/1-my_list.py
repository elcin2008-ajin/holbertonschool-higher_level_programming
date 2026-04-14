#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self.copy()))
