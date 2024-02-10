#!/usr/bin/python3
"""This module is to create a unittest for models/city.py"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def test_city_creation(self):
        """Test that a City object can be created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_has_attributes(self):
        """Test that a City object has all the expected attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_attributes_default_values(self):
        """Test that the default values of attributes are set correctly."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes_can_be_set(self):
        """Test that attributes of a City object can be set."""
        city = City()
        city.state_id = "state123"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
