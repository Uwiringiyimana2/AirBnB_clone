#!/usr/bin/python3
"""Tests class FileStorage"""
from models import storage
from models.base_model import BaseModel
import os
import unittest


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
