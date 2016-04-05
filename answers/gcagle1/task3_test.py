#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
29 March 2016
Assignment 16 Task 1

Developing unittests for Assignment 11 Task 3:
"A program taking a file as input and returning separate files containing all
the words starting with each letter of the alphabet, and their counts. The
first letter of the word is appended to the front of the file name."

'''

import unittest
import string
from collections import Counter
import os
import task3


class TestTask3(unittest.TestCase):

    def test_get_args(self):
        self.parser = task3.get_args()
        self.parsed = self.parser.parse_args('--infile word.txt')
        self.assertIs(type(self.parsed.infile), file)

    def test_remove_punct(self, args):
        self.args = task3.get_args()
        self.observed = task3.remove_punct(self.args)
        self.assertIs(type(self.observed), list)

    def test_write_file(self, args, histogram, letters):
        self.letters = list(string.ascii_lowercase)
        self.args = task3.get_args()
        self.histogram = dict(Counter(task3.remove_punct(self.args)))
        self.observed = task3.write_file(self.args, self.histogram, self.letters)
        self.assertIs(type(self.observed), file)

if __name__ == '__main__':
    unittest.main()
