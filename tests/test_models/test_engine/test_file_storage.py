#!/usr/bin/python3
"""Tests class FileStorage"""
from models import storage
from models.base_model import BaseModel
import os
import unittest
import models


class test_FileStorage(unittest.TestCase):
    """Tests class FileStorage"""

    def setUp(self):
        """setUp"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """tearDown"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual((storage.all()), {})

    def test_new(self):
        """New Object is correctly added to __objects"""
        new = BaseModel()
        temp = None
        objects = storage.all().values()
        if objects:
            for obj in objects:
                temp = obj
            self.assertTrue(temp is new)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """test reload method"""
        new = BaseModel()
        storage.new(new)
        loaded = None
        storage.save()
        storage.reload()
        for o in storage.all().values():
            loaded = o
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ reload an empty file """
        with open('file.json', "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_base_model_save(self):
        """ BaseModel save method calls save method"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ confirm __file_path is str"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_key_format(self):
        """ key is properly formatted"""
        new = BaseModel()
        _id = new.to_dict()['id']
        temp = None
        storage.new(new)
        storage.save()
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_type_objects(self):
        """confirm __objects id a dict"""
        self.assertEqual(type(storage.all()), dict)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
