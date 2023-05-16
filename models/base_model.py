#!/usr/bin/python3
"""
A BaseModel class that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialises the Basemodel class"""
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.created_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            Prints a dictionary representaion of the classname, id
            and dictionary
        """
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        baseDict = {}
        baseDict["_class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime, )):
                baseDict[key] = value.isoformat()
            else:
                baseDict[key] = value
        return baseDict
