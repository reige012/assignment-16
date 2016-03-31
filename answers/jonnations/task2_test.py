#!/usr/bin/env python
# utf-8

"""
Assignment 16, Task 2.
by Jon Nations on 29 March 2016

make an ordered dictionary of mass and species names of a bunch of
species from a genus.

Find the largest mass  (ordered like in other!)

find the smallest mass (other!)

find the average mass

find the median mass (must find number of keys in dict. )

"""

import unittest
import task2


class TestTask2(unittest.TestCase):

    def test_counting(self):
        observed = task2.counting('Big.Num')
        expected = 1
        self.assertEqual(observed, expected)

    def test_finder(self):
        observed = task2.finder('the coral')
        expected = 4
        self.assertEqual(observed, expected)

    def test_splits(self):
        observed = task2.splits('The.Coral')
        expected = ['The', 'Coral']
        self.assertEqual(observed, expected)

    def test_up(self):
        observed = task2.up('lowercase words')
        expected = ('LOWERCASE WORDS')
        self.assertEqual(observed, expected)

    def test_replacing(self):
        observed = task2.replacing("The")
        expected = ('DA')
        self.assertEqual(observed, expected)

if __name__ == '__main__':
    unittest.main()
