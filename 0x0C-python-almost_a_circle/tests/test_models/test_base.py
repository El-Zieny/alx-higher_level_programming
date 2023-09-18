#!/usr/bin/python3
""" a test for the base class"""
from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """A test class to test base class"""
    def test_init(self):
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)

        self.b2 = Base()
        self.assertEqual(self.b2.id, 2)

        self.b3 = Base()
        self.assertEqual(self.b3.id, 3)

        self.b4 = Base(7)
        self.assertEqual(self.b4.id, 7)

        self.b5 = Base()
        self.assertEqual(self.b4.id, 4)

if __name__ == '__main__':
    unittest.main()
