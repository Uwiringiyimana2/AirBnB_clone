#!/usr/bin/python3
"""This module defines class BaseModel that defines all common
    attributes/methods for other classes"""

from datetime import datetime
import uuid
import models


class BaseModel():
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes Public instance attributes

            Args:
                id: identifier
                created_at: current datetime when an instance is created
                updated_at: updated every time you change your object.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        a_dict = self.__dict__.copy()
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        a_dict['__class__'] = self.__class__.__name__
        return a_dict

    def __str__(self):
        """string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
