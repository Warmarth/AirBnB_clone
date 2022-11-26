#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances
    Private class attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of objects (__objects)
        """

        return type(self).__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (dict): objects to set self.__objects with.
        """
        objNameId = obj.__class__.__name__ + "." + obj.id
        type(self).__objects[objNameId] = obj

    def save(self):
        """
        Serializes objects (__objects) to Json file specified
        by file path (path: __file_path)
        """

        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            dict_storage = {}
            for key, val in type(self).__objects.items():
                dict_storage[key] = val.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the file
        does not exist, no exception should be raised)
        """
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                objdict = json.load(file)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
