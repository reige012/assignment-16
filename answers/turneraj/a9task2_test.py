#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 16 that tests the task 2 from Assignment 9.
 Helpful hints and collaboration provided by Mikey Henson, aka Pineapple House.

 Created by A.J. Turner on March 29, 2016.
"""
import unittest
import a9task2


class TestA9Task2(unittest.TestCase):

    def test_reformat(self):
        # lines longer than 80 ch b/c it wouldn't work otherwise....
        observed = a9task2.reformat('''I am very tired\tso very tired\nam I done\tI want to sleep\n''')
        expected = ['I am very tired,so very tired', 'am I done,I want to sleep', '']
        self.assertEqual(observed, expected)

if __name__ == '__main__':
    unittest.main()
