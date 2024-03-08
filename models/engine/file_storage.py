#!/usr/bin/python3
"""
    Model for the file storage
"""

import json

class FileStorage:
    """
        Defining FileStorage class that serializes
        instances to a JSON file and deserializes
        JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id

            Args:
                obj - instance object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        pass

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        pass
