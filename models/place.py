#!/usr/bin/python3
"""class Place"""

from models.base_model import BaseModel
from datetime import datetime
import pytz


class Place(BaseModel):
    """class Place inherit from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
