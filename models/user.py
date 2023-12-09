#!/usr/bin/python3
"""This modue creates a classn(user)"""
from models.base_model import BaseModel

class user(BaseModel):
    """This is a user class tHAT INHERITS FROM THE PArent class"""


    email = ""
    password = ""
    first_name = ""
    last_name = ""
