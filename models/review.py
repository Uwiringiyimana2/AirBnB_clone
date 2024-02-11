#!/usr/bin/python3
"""class Review"""

from models.base_model import BaseModel
from datetime import datetime
import pytz


class Review(BaseModel):
    """class Review"""

    place_id = ""
    user_id = ""
    text = ""
