#!/usr/bin/python3
"""This module for unittests for models/file_storage.py."""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def test_classes_method(self):
        """Test the classes method."""
        storage = FileStorage()
        classes = storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertIn('BaseModel', classes)
        self.assertIn('User', classes)
        self.assertIn('Place', classes)
        self.assertIn('State', classes)
        self.assertIn('City', classes)
        self.assertIn('Amenity', classes)
        self.assertIn('Review', classes)

    def test_get_attr_method(self):
        """Test the get_attr method."""
        storage = FileStorage()
        attributes = storage.get_attr()
        self.assertIsInstance(attributes, dict)
        self.assertIn('BaseModel', attributes)
        self.assertIn('User', attributes)
        self.assertIn('Place', attributes)
        self.assertIn('State', attributes)
        self.assertIn('City', attributes)
        self.assertIn('Amenity', attributes)
        self.assertIn('Review', attributes)

    def test_all_method(self):
        """Test the all method."""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """Test the new method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn('BaseModel.{}'.format(obj.id), storage.all())


if __name__ == '__main__':
    unittest.main()
