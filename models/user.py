#!/usr/bin/python3
"""This module defines class User"""

from models.base_model import BaseModel
from datetime import datetime
import pytz


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
