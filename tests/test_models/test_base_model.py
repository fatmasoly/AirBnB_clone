#!/usr/bin/python3
"""This module for unittests for models/basemodel.py."""

import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A test suite for the BaseModel class."""

    def test_init(self):
        """Test the initialization of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        """Test the save method of a BaseModel instance."""
        with patch('models.storage') as mock_storage:
            model = BaseModel()
            model.save()
            self.assertTrue(mock_storage.save.called)
            self.assertTrue(mock_storage.new.called)

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_kwargs(self):
        """Test the handling of keyword arguments
        in the BaseModel constructor."""
        model = BaseModel(name="Test", value=10)
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.value, 10)

    def test_kwargs_int(self):
        """Test the handling of integer keyword
        arguments in the BaseModel constructor."""
        model = BaseModel(value=10)
        self.assertEqual(model.value, 10)

    def test_str(self):
        """Test the string representation
        of a BaseModel instance."""
        model = BaseModel()
        self.assertEqual(str(model),
                         f"[BaseModel] ({model.id}) {model.__dict__}")

    def test_kwargs_none(self):
        """Test the behavior when no keyword arguments
        are passed to the BaseModel constructor."""
        model = BaseModel()
        self.assertNotIn('name', model.__dict__)
        self.assertNotIn('value', model.__dict__)

    def test_id(self):
        """Test the uniqueness of IDs
        generated for BaseModel instances."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """Test the creation timestamp
        attribute of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """Test the last updated timestamp
        attribute of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
