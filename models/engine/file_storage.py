#!/usr/bin/python3
"""
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json


class FileStorage():
    """
        class FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            if isinstance(type(cls), str):
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items:
                if isinstance(type(v), cls):
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        adict = {a: self.__objects[a].to_dict() for a in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(adict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o['__class__']
                    del o['__class__']
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
