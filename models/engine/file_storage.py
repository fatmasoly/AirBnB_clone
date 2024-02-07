#!/usr/bin/python3

import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            m_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(m_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                object_dict = json.load(file)
                for key, value in object_dict.items():
                    classs_name, _, object_id = key.partition(".")
                    classs = eval(classs_name)
                    obj = classs(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
