#!/usr/bin/python
"""This module defines class BaseModel that defines all common
    attributes/methods for other classes"""

import datetime
import pytz
import uuid


class BaseModel():
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes Public instance attributes

            Args:
                id: identifier
                created_at: current datetime when an instance is created
                updated_at: updated every time you change your object.
        """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        self.created_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        a_dict = self.__dict__
        a_dict['__class__'] = self.__class__.__name__
        return a_dict

    def __str__(self):
        """string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
