 #!/usr/bin/python3
 """class Amenity"""

 from models.base_model import BaseModel
 from datetime import datetime
 import pytz


 class Amenity(BaseModel):
     """class Amenity inherits from BaseModel"""

     name = ""
