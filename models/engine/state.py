#!/usr/bin/python3
"""This module creates a state clas that inherits from parent class BASEMODEL"""

from models.base_model import BaseModel


class State(BaseModel):
    """This is the class for managing state objects"""

    name = ""
