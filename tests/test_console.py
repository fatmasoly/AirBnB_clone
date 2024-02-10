#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from models import storage
from console import fix_dict


class TestUpdateDict(unittest.TestCase):
    """A test suite for the fix_dict function."""

    @patch('builtins.print')
    def test_invalid_json_format(self, mock_print):
        """Test behavior when JSON format is invalid."""
        fix_dict("TestClass", "123", "invalid_json")
        mock_print.assert_called_once_with("** Invalid JSON format **")

    @patch('builtins.print')
    def test_class_name_missing(self, mock_print):
        """Test behavior when class name is missing."""
        fix_dict("", "123", '{"name": "test"}')
        mock_print.assert_called_once_with("** class name missing **")

    @patch('builtins.print')
    def test_class_not_exist(self, mock_print):
        """Test behavior when class does not exist."""
        storage.classes = MagicMock(return_value=[])
        fix_dict("NonExistentClass", "123", '{"name": "test"}')
        mock_print.assert_called_once_with("** class doesn't exist **")

    @patch('builtins.print')
    def test_instance_id_missing(self, mock_print):
        """Test behavior when instance ID is missing."""
        fix_dict("TestClass", None, '{"name": "test"}')
        mock_print.assert_called_once_with("** instance id missing **")

    @patch('builtins.print')
    def test_no_instance_found(self, mock_print):
        """Test behavior when no instance is found."""
        storage.all = MagicMock(return_value={})
        fix_dict("TestClass", "123", '{"name": "test"}')
        mock_print.assert_called_once_with("** no instance found **")

    @patch('builtins.print')
    def test_update_attributes(self, mock_print):
        """Test updating attributes of an instance."""
        instance = MagicMock()
        storage.all = MagicMock(return_value={"TestClass.123": instance})
        storage.classes = MagicMock(return_value={"TestClass": {"name": str}})
        fix_dict("TestClass", "123", '{"name": "updated_name"}')
        instance.save.assert_called_once()
        self.assertEqual(instance.name, "updated_name")

    @patch('builtins.print')
    def test_attribute_conversion(self, mock_print):
        """Test attribute conversion during update."""
        instance = MagicMock()
        storage.all = MagicMock(return_value={"TestClass.123": instance})
        storage.classes = MagicMock(return_value={"TestClass": {"value": int}})
        fix_dict("TestClass", "123", '{"value": "42"}')
        instance.save.assert_called_once()
        self.assertEqual(instance.value, 42)


if __name__ == '__main__':
    unittest.main()
