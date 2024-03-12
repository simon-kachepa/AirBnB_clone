#!/usr/bin/python3
"""
    Model for the file storage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        obj_dictionary = {}

        for key, value in self.all().items():
            obj_dictionary[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as text_file:
            json.dump(obj_dictionary, text_file)

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """

        from models.base_model import BaseModel
        from models.user import User

        class_map = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
            }

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as text_file:
                obj_dictionary = json.load(text_file)

                for key, val in obj_dictionary.items():
                    class_name = val['__class__']
                    class_instance = class_map[class_name]
                    instance = class_instance(**val)
                    all_objects = self.all()
                    all_objects[key] = instance
        except FileNotFoundError:
            pass
