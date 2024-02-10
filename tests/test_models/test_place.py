#!/usr/bin/python3
"""This module is to create a unitest for models/Place.py"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class."""

    def test_place_creation(self):
        """Test that a Place object can be created."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_has_attributes(self):
        """Test that a Place object has all the expected attributes."""
        place = Place()
        attributes = ['city_id', 'user_id', 'name', 'description',
                      'number_rooms', 'number_bathrooms', 'max_guest',
                      'price_by_night', 'latitude', 'longitude', 'amenity_ids']
        for attr in attributes:
            self.assertTrue(hasattr(place, attr))

    def test_place_attributes_default_values(self):
        """Test that the default values of attributes are set correctly."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attributes_can_be_set(self):
        """Test that attributes of a Place object can be set."""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user456"
        place.name = "Cozy Cottage"
        place.description = "A charming cottage in the countryside."
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 51.5
        place.longitude = -0.1
        place.amenity_ids = ['amenity1', 'amenity2']
        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user456")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description,
                         "A charming cottage in the countryside.")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 51.5)
        self.assertEqual(place.longitude, -0.1)
        self.assertEqual(place.amenity_ids, ['amenity1', 'amenity2'])


if __name__ == '__main__':
    unittest.main()
