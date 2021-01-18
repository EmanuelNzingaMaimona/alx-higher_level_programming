#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
