#!/usr/bin/python3
"""
Unittest cases for the console module
"""

import unittest
from io import StringIO
import sys
from console import HBNBCommand
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """
    Defines unittest cases for the HBNB Command Interpreter console
    """

    def setUp(self):
        """Set up the test for testing the console."""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Remove setups after test."""
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_help_command(self):
        """Test that help command displays correct output."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Exits the program with formatting",
                          f.getvalue().strip())

    def test_empty_line(self):
        """Test that empty line does nothing."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_quit(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_EOF(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")

    def test_create_missing_class(self):
        """Test create with missing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_create_no_class(self):
        """Test create with nonexistent class."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_no_args(self):
        """Test show command with no arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_show_no_id(self):
        """Test show command with missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
