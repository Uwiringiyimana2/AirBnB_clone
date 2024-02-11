#!/usr/bin/python3
"""Tests class State"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_State(test_basemodel):
    """Tests class State"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
