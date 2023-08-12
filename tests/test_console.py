#!/usr/bin/python3
"""Defines unitests for console.py

Unittest classses:
        TestHBNBCommand_create
"""

import os
import sys
import unittest

from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_object_params(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create State name=\"California\""
                )
            )
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
            self.assertEqual("California", storage.all()[testKey].name)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create State name=\"Arizona\""
                )
            )
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
            self.assertEqual("Arizona", storage.all()[testKey].name)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create Place city_id=\"0001\" \
                user_id=\"0001\" name=\"My_little_house\" number_rooms=4 \
                number_bathrooms=2 max_guest=10 \
                price_by_night=300 latitude=37.773972 \
                longitude=-122.431297"
                )
            )
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
            self.assertEqual("My little house", storage.all()[testKey].name)
            self.assertEqual("0001", storage.all()[testKey].city_id)
            self.assertEqual("0001", storage.all()[testKey].user_id)
            self.assertEqual(4, storage.all()[testKey].number_rooms)
            self.assertEqual(2, storage.all()[testKey].number_bathrooms)
            self.assertEqual(10, storage.all()[testKey].max_guest)
            self.assertEqual(300, storage.all()[testKey].price_by_night)
            self.assertEqual(37.773972, storage.all()[testKey].latitude)
            self.assertEqual(-122.431297, storage.all()[testKey].longitude)
