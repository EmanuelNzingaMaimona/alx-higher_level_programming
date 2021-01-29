#!/usr/bin/python3
"""This module is for the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class to inherit from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates multiples attributes as either args or dicts
        Args:
            *args: multiple arguments
            **kwargs: dictionary arguments
        """
        attr = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
