#!/usr/bin/python3
"""This module is for unittests for console."""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """a class to test console"""
    def setUp(self):
        """Set up the test environment before each test method is run."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment after each test method is run."""
        pass

    def test_help_show(self):
        """Test the 'help show' command.

    This test checks if the 'help show' command displays help information
    related to the 'show' command functionality.
    """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
        output = f.getvalue().strip()
        print("Actual help output:", output)

    def test_create_instance(self):
        """Test the 'create' command for creating a new instance.

        This test checks if the 'create' command successfully creates
        a new instance of the specified class and returns the instance ID.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_instance(self):
        """Test the 'show' command for displaying an instance.

        This test checks if the 'show' command correctly displays the
        string representation of the specified instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output_create = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(output_create))
            output_show = f.getvalue().strip()
            self.assertTrue("BaseModel" in output_show)
            self.assertTrue(output_create in output_show)

    def test_destroy_instance(self):
        """Test the 'destroy' command for destroying an instance.

        This test checks if the 'destroy' command successfully removes
        the specified instance from storage.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output_create = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(output_create))
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(output_create))
            output_show = f.getvalue().strip()
            self.assertEqual(output_show, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
