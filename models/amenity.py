#!/usr/bin/python3
"""This module is to create an Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity available in a place.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
