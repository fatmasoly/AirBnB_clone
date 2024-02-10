#!/usr/bin/python3
"""This module for unittests for models/user.py."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """A test suite for the User class."""

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test that User has the correct attributes."""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_attribute_types(self):
        """Test that the attributes of User have the correct types."""
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_initialization(self):
        """Test that an instance of User can be initialized."""
        user = User()
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
