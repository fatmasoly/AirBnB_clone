#!/usr/bin/python3
"""This Module is for the FileStorage class."""
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
    """A class for storing and managing serialized
    objects in JSON format.

    Attributes:
        __file_path (str): The path to the JSON file
        storing serialized objects.
        __objects (dict): A dictionary containing serialized objects.
    """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of available model classes.

        Returns:
            dict: A dictionary mapping class names to their
            corresponding model classes.
        """
        classes = {'BaseModel': BaseModel,
                   'User': User,
                   'Place': Place,
                   'State': State,
                   'City': City,
                   'Amenity': Amenity,
                   'Review': Review}
        return classes

    def get_attr(self):
        """Returns a dictionary of attributes for each model class.

        Returns:
            dict: A dictionary mapping class names to
            dictionaries of their attributes.
        """
        attributes = {
            "BaseModel": {"id": str, "created_at": datetime.datetime,
                          "updated_at": datetime.datetime},
            "User": {"email": str, "password": str, "first_name": str,
                     "last_name": str},
            "Review": {"place_id": str, "user_id": str, "text": str},
            "City": {"state_id": str, "name": str},
            "Place": {"city_id": str, "user_id": str, "name": str,
                      "description": str, "number_rooms": int,
                      "number_bathrooms": int, "max_guest": int,
                      "price_by_night": int, "latitude": float,
                      "longitude": float, "amenity_ids": list},
            "State": {"name": str},
            "Amenity": {"name": str}
            }
        return attributes

    def all(self):
        """Returns the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing all serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new serialized object to the dictionary of objects.

        Args:
            obj: The object to be serialized and added to the dictionary.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes and saves the objects dictionary to a JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            m_dict = {key: value.to_dict()
                      for key, value in FileStorage.__objects.items()}
            json.dump(m_dict, file)

    def reload(self):
        """Deserializes and reloads the objects from the JSON file."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                object_dict = json.load(file)
            for key, value in object_dict.items():
                if key == "__class__":
                    continue
                class_name, _, object_id = key.partition(".")
                class_ = eval(class_name)
                obj = class_(**value)
                for k, v in value.items():
                    if k == "created_at" or k == "updated_at":
                        v = datetime.datetime.fromisoformat(v)
                        setattr(obj, k, v)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
