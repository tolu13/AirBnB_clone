#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime

class BaseModel:
	"""This is the parent class in which other class inherits from"""
	def __init__(self):
	    """This initializes instance attributes"""
	    self.id = str(uuid.uuid4())
	    self.created_at = datetime.now()
	    self.updated_at = datetime.now()

	def __str__(self):
	    """this returns official string representation"""
	    return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

	def save(self):
	    """update the public instance attributes"""
	    self.updated_at = datetime.now()

	def to_dict(self):
	    """this returns dictionary containing key/value"""
	    obj_dict = self.__dict__.copy()
	    obj_dict['__class__'] = self.__class__.__name__
	    obj_dict['created_at'] = self.created_at.isoformat()
	    obj_dict['updated_at'] = self.updated_at.isoformat()
	    return obj_dict