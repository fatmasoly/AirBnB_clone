#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.console.stdout = StringIO()

    def tearDown(self):
        self.console.stdout.close()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")
        self.assertIsInstance(output, str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        obj_id = output.split()[-1]
        self.console.onecmd(f'show BaseModel {obj_id}')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")
        self.assertIsInstance(output, str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        obj_id = output.split()[-1]
        self.console.onecmd(f'destroy BaseModel {obj_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        self.console.onecmd('all')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output != "")
        self.assertIsInstance(output, str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        self.console.onecmd('count BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.isdigit())
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.console.onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        obj_id = output.split()[-1]
        self.console.onecmd(f'update BaseModel {obj_id} name "new_name"')
        self.console.onecmd(f'show BaseModel {obj_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn('new_name', output)

    def test_fix_dict(self):
        pass


if __name__ == '__main__':
    unittest.main()

# import unittest
# from unittest.mock import patch, MagicMock
# from models import storage


# class TestUpdateDict(unittest.TestCase):
#     """A test suite for the fix_dict function."""

#     @patch('builtins.print')
#     def test_invalid_json_format(self, mock_print):
#         """Test behavior when JSON format is invalid."""
#         fix_dict("TestClass", "123", "invalid_json")
#         mock_print.assert_called_once_with("** Invalid JSON format **")

#     @patch('builtins.print')
#     def test_class_name_missing(self, mock_print):
#         """Test behavior when class name is missing."""
#         fix_dict("", "123", '{"name": "test"}')
#         mock_print.assert_called_once_with("** class name missing **")

#     @patch('builtins.print')
#     def test_class_not_exist(self, mock_print):
#         """Test behavior when class does not exist."""
#         storage.classes = MagicMock(return_value=[])
#         fix_dict("NonExistentClass", "123", '{"name": "test"}')
#         mock_print.assert_called_once_with("** class doesn't exist **")

#     @patch('builtins.print')
#     def test_instance_id_missing(self, mock_print):
#         """Test behavior when instance ID is missing."""
#         fix_dict("TestClass", None, '{"name": "test"}')
#         mock_print.assert_called_once_with("** instance id missing **")

#     @patch('builtins.print')
#     def test_no_instance_found(self, mock_print):
#         """Test behavior when no instance is found."""
#         storage.all = MagicMock(return_value={})
#         fix_dict("TestClass", "123", '{"name": "test"}')
#         mock_print.assert_called_once_with("** no instance found **")

#     @patch('builtins.print')
#     def test_update_attributes(self, mock_print):
#         """Test updating attributes of an instance."""
#         instance = MagicMock()
#         storage.all = MagicMock(return_value={"TestClass.123": instance})
#         storage.classes = MagicMock(return_value={"TestClass": {"name": str}})
#         fix_dict("TestClass", "123", '{"name": "updated_name"}')
#         instance.save.assert_called_once()
#         self.assertEqual(instance.name, "updated_name")

#     @patch('builtins.print')
#     def test_attribute_conversion(self, mock_print):
#         """Test attribute conversion during update."""
#         instance = MagicMock()
#         storage.all = MagicMock(return_value={"TestClass.123": instance})
#         storage.classes = MagicMock(return_value={"TestClass": {"value": int}})
#         fix_dict("TestClass", "123", '{"value": "42"}')
#         instance.save.assert_called_once()
#         self.assertEqual(instance.value, 42)


# if __name__ == '__main__':
#     unittest.main()
