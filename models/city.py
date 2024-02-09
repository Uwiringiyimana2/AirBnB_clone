#!/usr/bin/python3
"""class City"""

from models.base_model import BaseModel
from datetime import datetime
import pytz


class City(BaseModel):
    """class City that inherit from BaseModel"""

    state_id = ""
    name = ""
