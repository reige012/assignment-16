#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 16 Task 1

Developing unittests for Assignment 11 Task 3:
"A program taking a file as input and returning separate files containing all
the words starting with each letter of the alphabet, and their counts. The
first letter of the word is appended to the front of the file name."

'''

import sys
import unittest
import task3


class TestTask3(unittest.TestCase):

    def test_get_args(self):
        observed = task3.get_args()
        expected = sys.argv[0]
        self.assertEqual(observed, expected)

    def test_remove_punct(self, args):
        observed = task3.remove_punct(args)
        self.assertIsInstance(observed, list)

    def test_write_file(self, args, histogram, letters):
        observed = task3.write_file(args, histogram, letters)
        self.assertIsInstance(observed, file)

if __name__ == '__main__':
    unittest.main()
