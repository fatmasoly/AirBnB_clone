#!/usr/bin/python3
"""This module is to create a unittest for models/review.py"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def test_review_creation(self):
        """Test that a Review object can be created."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_has_attributes(self):
        """Test that a Review object has all the expected attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_attributes_default_values(self):
        """Test that the default values of attributes are set correctly."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes_can_be_set(self):
        """Test that attributes of a Review object can be set."""
        review = Review()
        review.place_id = "place123"
        review.user_id = "user456"
        review.text = "Great place to stay!"
        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user456")
        self.assertEqual(review.text, "Great place to stay!")


if __name__ == '__main__':
    unittest.main()
