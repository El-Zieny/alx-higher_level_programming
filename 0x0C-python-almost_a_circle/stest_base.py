#!/usr/bin/python3
""" module for test base class """

from models.base import Base
from unittest import TestCase, main


class testBaseMethods(TestCase):
    """suite to test Base class """

    def setUp(self):
        Base._base__nb_objects = 0

    def tearDown(
