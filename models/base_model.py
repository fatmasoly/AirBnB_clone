#!/usr/bin/python3
"""This script is for class BaseModel that defines
    all common attributes/methods for other classes"""

import uuid
import datetime
import models


class BaseModel:
    """Defines the base model class for
    other classes to inherit from."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime
                    (kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime
                    (kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the instance's updated_at attribute and save the changes."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        this_dict = self.__dict__.copy()
        this_dict["created_at"] = datetime.datetime.isoformat(self.created_at)
        this_dict["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        this_dict["__class__"] = type(self).__name__
        return this_dict
