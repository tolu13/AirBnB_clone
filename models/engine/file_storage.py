#!/usr/bin/python3
""" This is the module for filestorage class"""
import json
import datetime
import os

class FileStorage:
	"""This class is for storing and retrieving data"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
	
		"""This returns the dictionary objects"""
		return FileStorage.__objects

	def new(self, obj):
		"""This  sets in __objects the obj with key <obj class name>.id"""
		key = "{}.{}".format(type(obj).__name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		"""This serializes objects..... into the json file"""
		serialized_obj = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
		with open (self.__file_path, 'w', encoding='utf-8' ) as file:
			json.dump(serialized_obj, file)

	def classes(self):
                """This returns the dictionary representation of  class attributes"""
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review
                from models.place import Place

                classes = {"BaseModel": BaseModel,
                           "User": User,
                           "State": State,
                           "City": City,
                           "Amenity": Amenity,
                           "Review": Review,
                           "Placd": Place}
                return classes 
	def reload(self):
	        """This reloads the stored objects"""
	        if not os.path.isfile(FileStorage.__file_path):
                   return
	        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                    obj_dict = json.load(file)
                    obj_dict = {key: self.classes()[value["__class__"]](**value)
                                for key, value in obj_dict.items()}
                    # TODO: should this overwrite or insert?
                    FileStorage.__objects = obj_dict
      
	def attributes(self):
		"""This returns the valid attributes and their types and classname"""
		attributes = {
		"BaseModel":
			{"id": str,
			"created_at": datetime.datetime,
			"updated_at": datetime.datetime},
		"User":
			{"email": str,
			"password": str,
			"first_name": str,
			"last_name": str},
		"State":
			{"name": str},
		"City":
			{"state_id": str,
			"name": str},
		"Amenity":
			{"name": str},
		"Place":
			{"city_id": str,
			"user_id": str,
			"name": str,
			"description": str,
			"number_rooms": int,
			"number_bathrooms": int,
			"max_guest": int,
			"price_by_night": int,
			"latitude": float,
			"longitude": float,
			"amenity_ids": list},
		"Review":
			{"place_id": str,
			"user_id": str,
			"text": str}
		}
		return attributes
