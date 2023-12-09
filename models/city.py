#!/usr/bin/python3
"""This module creates a User city class that inherits from parent class BASEMODEl"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the class for managing city objects"""

    state_id = ""
    name = ""
