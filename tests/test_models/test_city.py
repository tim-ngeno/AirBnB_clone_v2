#!/usr/bin/python3
"""Unittest for the City module"""

import unittest
from models.city import City
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class TestCity(unittest.TestCase):
    """Defines tests for the City class"""

    @classmethod
    def setUpClass(cls):
        """Sets up objects for testing"""
        cls.city1 = City()
        cls.city1.name = "San Francisco"
        cls.city1.state_id = "CA_001"

    @classmethod
    def tearDownClass(cls):
        """Tears down testing environment"""
        del cls.city1
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertIsInstance(self.city1, BaseModel)
        self.assertIsInstance(self.city1, City)

    def test_columns(self):
        """Test if City class has columns"""
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))

    def test_attributes_types(self):
        """Test attribute type for City"""
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_checking_for_functions(self):
        """Test if there are methods available in City"""
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Test if City has attributes"""
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertTrue(hasattr(self.city1, "state_id"))

    def test_attributes_are_strings(self):
        """Test if City attributes are strings"""
        self.assertTrue(isinstance(self.city1.name, str))
        self.assertTrue(isinstance(self.city1.state_id, str))

    def test_save(self):
        """Test if save method updates the updated_at attribute"""
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """Test if dictionary returned by to_dict is accurate"""
        self.assertEqual('to_dict' in dir(self.city1), True)

    def test_relationships(self):
        """Test the relationships in City class"""
        self.assertEqual(hasattr(self.city1, "state_id"), True)


if __name__ == "__main__":
    unittest.main()
