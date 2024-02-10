#!/usr/bin/python3
"""This module for unittests for models/amenity.py."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """A test suite for the Amenity class."""

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test that Amenity has the correct attributes."""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_attribute_types(self):
        """Test that the attributes of Amenity have the correct types."""
        self.assertIsInstance(Amenity.name, str)

    def test_initialization(self):
        """Test that an instance of Amenity can be initialized."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
