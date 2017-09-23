## A simple unit test example. Replace by your own tests
# https://docs.python.org/2/library/unittest.html


import sys
import unittest

from calc import *

class MyTest(unittest.TestCase):

    def test_reg(self):
        r = Register()
        self.assertEqual(r.get(), 0)
        r.add(1)
        self.assertEqual(r.get(), 1)
        r.sub(3)
        self.assertEqual(r.get(), -2)
        r.reset()
        self.assertEqual(r.get(), 0)

    def test_parser(self):
        self.assertEqual(parse_line('+ 10'), ('+', 10))

        with self.assertRaises(Exception):
            parse_line('+ 10 20')

        with self.assertRaises(Exception):
            parse_line('\n')

        with self.assertRaises(Exception):
            parse_line('* 20')

        with self.assertRaises(Exception):
            parse_line('+ ten')

        with self.assertRaises(Exception):
            parse_line ('c 10')

    def test_upper(self):
        """Test the upper() function of class string"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Test isupper() function of class string"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_exception(self):
        with self.assertRaises(Exception):
            raise Exception('Error')


if __name__ == '__main__':
    unittest.main()
