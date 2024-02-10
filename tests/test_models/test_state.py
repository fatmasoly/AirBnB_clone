#!/usr/bin/python3
"""This module is to create a unittests for models/State.py."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def test_state_creation(self):
        """Test that a State object can be created."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_has_name_attribute(self):
        """Test that a State object has a 'name' attribute."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_name_is_empty_string_by_default(self):
        """Test that the 'name' attribute of a State
        object is an empty string by default."""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_can_be_set(self):
        """Test that the 'name' attribute of a State object can be set."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
