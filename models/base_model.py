#!/usr/bin/python3
"""
It defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""


    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel class.

        Args:
            *args (any): anonymous arguments (unused)
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if any(kwargs):
            dt_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, dt_format)
                setattr(self, key, value)
        else:
            models.storage.new(self)


    def save(self):
        """
        Updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        clsName = self.__class__.__name__
        classDict = self.__dict__.copy()
        classDict['updated_at'] = self.updated_at.isoformat()
        classDict['created_at'] = self.created_at.isoformat()
        classDict['__class__'] = clsName

        return classDict


    def __str__(self):
        """
        Representation of BaseModel instances
        """

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)
