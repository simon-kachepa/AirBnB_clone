#!/usr/bin/pyhton3
"""
Module for creating a user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defining a User class that creates a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
