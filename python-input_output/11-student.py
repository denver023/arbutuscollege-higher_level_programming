#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary representation of Student

        Args:
            attrs (list): List of strings of attribute names to include
                         If None, all attributes are included

        Returns:
            dict: Dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json (dict): Dictionary where key is the public attribute name
                        and value is the value of the public attribute
        """
        for key, value in json.items():
            setattr(self, key, value)
