#!/usr/bin/pyton3
"""Store first object"""
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.city import City 
from models.review import Review
from models.state import State


class FileStorage:
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User, "Amenity": Amenity,
        "Place": Place, "City": City, "Review": Review,
        "State": State
        }

    def all(self):
        """Returns the dictionary """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        if obj:
            objKey = "{}.{}".format(
                obj.__class__.__name__, obj.id)
            self.__objects[objKey] = obj

    def save(self):
        """
            Serializes __objects to the JSON file
            (path: __file_path)
        """
        newDict = {}
        with open(self.__file_path, mode='w', encoding='UTF-8') as fil:
            for key, value in self.__objects.items():
                newDict[key] = value.to_dict()
            json.dump(newDict, fil)

    def reload(self):
        """
            Deserializes the JSON file to
            __objects (only if the JSON file
        """
        try:
            new_obj = {}
            with open(self.__file_path, mode="r", encoding='UTF-8') as fil:
                for key, value in json.load(fil).items():
                    new_obj = self.class_dict[value['__class__']](**value)
                    self.__objects[key] = new_obj
        except FileNotFoundError:
            pass
