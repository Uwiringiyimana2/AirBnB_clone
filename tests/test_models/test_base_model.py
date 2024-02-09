#!/usr/bin/python3
"""unittest of class BaseModel"""

import datetime
import pytz
import uuid
from models.base_model import BaseModel
import unittest
import json
import os


class test_basemodel(unittest.TestCase):
    """unittest of class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Tests instatiation of Base"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """setUp"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_str(self):
        """str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))

    def test_created_at(self):
        """created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        new.my_number = 90
        new.save()
        self.assertFalse(new.created_at == new.updated_at)

    def test_id(self):
        """id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_to_dict(self):
        """to_dict"""
        new = self.value()
        o = new.to_dict()
        self.assertEqual(type(o), dict)
        self.assertEqual(new.to_dict(), o)

    def test_save(self):
        """save"""
        new = self.value()
        new.save()
        key = self.name + '.' + new.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], new.to_dict())

    def test_kwargs(self):
        """kwargs"""
        o = self.value()
        copy = o.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is o)

    def test_kwargs_int(self):
        """int kwargs"""
        o = self.value()
        copy = o.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_none(self):
        """none as kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

#    def test_kwargs_one(self):
 #       """one kwargs"""
  #      n = {}
   #     with self.assertRaises(KeyError):
    #        new = self.value(**n)
