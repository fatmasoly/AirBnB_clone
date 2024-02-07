#!/usr/bin/python3

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        this_dict = self.__dict__.copy()
        this_dict["__class__"] = self.__class__.__name__
        this_dict["created_at"] = this_dict["created_at"].isoformat()
        this_dict["updated_at"] = this_dict["updated_at"].isoformat()
        return this_dict
