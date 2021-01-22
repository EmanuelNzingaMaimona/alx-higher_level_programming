#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
         """Get a dictionary representation of the Student."""
        if attrs==None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i is in self.__dict__.keys():
                dic[i] = self.__dict__[i]
        return dic
    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            self.__dict__[key] = value
