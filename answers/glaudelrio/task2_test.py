# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:20:33 2016

@author: Glaucia
"""

import unittest

import task2


class Task2Test(unittest.TestCase):
    def test1_reading_csv_files(self):
        observed = task2.reading_csv_files("Rheg.csv")[0]
        expected = ['Bnumber', 'Species', 'DNA_concentration']
        self.assertEqual(observed, expected)

    def test2_c2v2(self):
        observed = task2.c2v2(3, 3)
        expected = 9
        self.assertEqual(observed, expected)

    def test3_concentration_in_list(self):
        observed = task2.concentration_in_list([['1', '2', '3'],
                                               ['x', 'y', 'z'],
                                               [1, 2, 3]], 2)
        expected = [3.0, 3.0]
        self.assertEqual(observed, expected)

    def test4_DNA_volume(self):
        observed = task2.DNA_volume([2, 4, 8], 2)
        expected = [1, 0.5, 0.25]
        self.assertEqual(observed, expected)

    def test5_buffer_volume(self):
        observed = task2.buffer_volume([10, 20, 15], 50)
        expected = [40, 30, 35]
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
