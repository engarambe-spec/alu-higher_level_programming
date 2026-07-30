#!/usr/bin/python3
"""Module that defines the Base class"""
import json


class Base:
    """Represents the base class of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base

        Args:
            id: the identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dicts

        Args:
            list_dictionaries: a list of dictionaries

        Returns:
            A JSON string, or "[]" if list_dictionaries is None or empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects
        to a file

        Args:
            list_objs: a list of instances that inherit from Base
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by a JSON string of dicts

        Args:
            json_string: a string representing a list of dictionaries

        Returns:
            The list represented by json_string, or an empty list if
            json_string is None or empty
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary: key/value pairs of attributes to set

        Returns:
            A new instance of cls with the given attributes applied
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file

        The filename is based on the class name: <Class name>.json

        Returns:
            A list of instances of cls, or an empty list if the file
            doesn't exist
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
