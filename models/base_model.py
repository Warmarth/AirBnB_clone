#!/usr/bin/python3
"""

 defining the BaseModel Class

"""

import model
from datetime import datetime
from uuid import uuid4


class BaseModel():

    def __init__(self,*args,**kwargs):
        

    def id(self,id,uuid):
        self.id = id
        self.uuid = uuid



