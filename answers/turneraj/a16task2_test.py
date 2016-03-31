#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 16 that tests the task 2 file (program)from
 Assignment 16. Helpful hints and collaboration provided by Mikey Henson, aka
 Pineapple House, and S. Shaky.

 Apparently when comparing dataframes, they need to be converted to a string
 because otherwise they contain too many "things" (columns/rows) that have to
 be compared between them (and python can't handle that??). This was figured
 out by S. Shaky--I could not figure it out for the life of me.

 Created by A.J. Turner on March 30, 2016.
"""
import unittest
import a16task2
import pandas


class TestA16Task2(unittest.TestCase):

    def test_sortme(self):
        df = pandas.read_csv('test_file.csv', index_col=0)
        observed = a16task2.sortme(df)
        expected = pandas.read_csv('expected_sort.csv', index_col=0)
        self.assertEqual(str(observed), str(expected))

    def test_col_del(self):
        df = pandas.read_csv('test_file.csv', index_col=0)
        observed = a16task2.col_del(df)
        expected = pandas.read_csv('expected_col_del.csv', index_col=0)
        self.assertEqual(str(observed), str(expected))

    def test_rep_value(self):
        df = pandas.read_csv('test_file.csv', index_col=0)
        observed = a16task2.rep_value(df)
        expected = pandas.read_csv('expected_rep_value.csv', index_col=0)
        self.assertEqual(str(observed), str(expected))

    def test_sumit(self):
        df = pandas.read_csv('test_file.csv', index_col=0)
        observed = a16task2.sumit(df)
        expected = 10568
        self.assertEqual(observed, expected)

    def test_new_name(self):
        df = pandas.read_csv('test_file.csv', index_col=0)
        observed = a16task2.new_name(df)
        expected = pandas.read_csv('expected_new_name.csv', index_col=0)
        self.assertEqual(str(observed), str(expected))


if __name__ == '__main__':
    unittest.main()
