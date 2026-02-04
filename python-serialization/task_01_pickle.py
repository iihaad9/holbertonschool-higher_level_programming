#!/usr/bin/python3
"""Pickle serialization for a custom class."""


import pickle


class CustomObject:
    """Custom object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None
        return self

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if not isinstance(obj, cls):
                return None
            return obj
        except Exception:
            return None
