#!/usr/bin/python3
"""Tests HBNBCommand module"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch


class test_HBNBCommand(unittest.TestCase):
    """tests command interpreter"""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
