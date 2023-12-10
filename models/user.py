#!/usr/bin/python3
"""This module creates a class (User)"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is a User class that inherits from the parent class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
