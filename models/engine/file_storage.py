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
	def reload(self):
        """This reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(f)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict#!
