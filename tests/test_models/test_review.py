#!/usr/bin/python3
"""Tests class Review"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_Review(test_basemodel):
    """Tests class Review"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'Review'
        self.value = Review

    def test_place_id(self):
        """Is place_id a str"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
