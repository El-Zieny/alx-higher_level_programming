#!/usr/bin/python3
""" a test for the base class"""
from unittest import TestCase
import models.base as b
import models.square as s
import models.rectangle as r


class TestBase(TestCase):
    """A test class to test base class"""
    def test_module_doc(self):
        """test for module doc"""
        self.assertIsNotNone(b.__doc__)
        self.assertGreater(len(b.__doc__), 0)

    def test_class_doc(self):
        """test for the class doc"""
        self.assertIsNotNone(b.Base.__doc__)
        self.assertGreater(len(b.Base.__doc__), 0)

    def test_method_doc(self):
        """test for the __init__ doc"""
        self.assertIsNotNone(b.Base.__init__.__doc__)
        self.assertGreater(len(b.Base.__init__.__doc__), 0)

    def test_to_json_string_doc(self):
        """test for the to string doc"""
        self.assertIsNotNone(b.Base.to_json_string.__doc__)
        self.assertGreater(len(b.Base.to_json_string.__doc__), 0)
    
    def setUp(self):
        """resets counter and create a tepmorary directory for test files"""
        b.Base._Base__nb_object = 0

    def test_base_id_incr(self):
        """test for the base id increment"""
        b1 = b.Base()
        b2 = b.Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_None(self):
        """test for None id"""
        b1 = b.Base(None)
        b2 = b.Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_private_attribute(self):
        """test for private attributes"""
        with self.assertRaises(AttributeError):
            b.Base(5).__nb_objects

    def test_id_true(self):
        """tests id boolean"""
        self.assertEqual(b.Base(True).id, True)
"""
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
"""
if __name__ == '__main__':
    unittest.main()
