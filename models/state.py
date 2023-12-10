#!/usr/bin/python3
"""This module creates state clas that inherit from parent class BASEMODEL"""

from models.base_model import BaseModel


class State(BaseModel):
    """This is the class for managing state objects"""

    name = ""
