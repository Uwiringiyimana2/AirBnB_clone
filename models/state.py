#!/usr/bin/python3
"""class State"""

from models.base_model import BaseModel
from datetime import datetime
import pytz


class State(BaseModel):
    """class State that inherit from BaseModel"""

    name = ""
