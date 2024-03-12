#!/usr/bin/python3
"""
    Defining the Base Class Module
    - Public instance attributes
        - id- string
        - created_at - datetime
        - updated_at - datetime
    - Public instant methods
        - save(self) - updates the public instance attribute
                        updated_at with the current datetime
        - to_dict(self) - returns a dictionary containing all
                        keys/values of __dict__ of the instance
    Linking BaseModel to FileStorage using the variable storage
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
        This is the Base class that defines all common
        attributes/methods for other classes and all
        other classes will inherit from this class
    """

    def __init__(self, *args, **kwargs):
        """
            Initializing the new instance of the BaseModel

            Args:
                args: Unused argument
                kwargs: Dictionary representation of the current instance
        """
        if kwargs:
            if kwargs["__class__"]:
                del kwargs["__class__"]
            if kwargs["created_at"]:
                nw_ft = "%Y-%m-%dT%H:%M:%S.%f"
                new_cr_date = datetime.strptime(
                                                kwargs[
                                                        "created_at"], nw_ft)
                kwargs["created_at"] = new_cr_date
            if kwargs["updated_at"]:
                nw_ft = "%Y-%m-%dT%H:%M:%S.%f"
                new_up_date = datetime.strptime(
                                                kwargs[
                                                        "updated_at"], nw_ft)
                kwargs["updated_at"] = new_up_date

            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            Represent the string representation of the currect object
        """

        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime
        """
        updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        new_dictionary = self.__dict__

        new_dictionary["__class__"] = self.__class__.__name__
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()

        return (new_dictionary)
