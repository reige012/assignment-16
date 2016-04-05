#!/usr/bin/env python
# encoding: utf-8
"""
assignment 16.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import unittest
import Task1


class TestTask1(unittest.TestCase):

    def test_count(self):
        observed = Task1.count('People Are Awesome ... !!!')
        self.assertEqual(observed, 5)

    def test_upper(self):
        observed = Task1.upper('People Are Awesome ... !!!')
        expected = 'PEOPLE ARE AWESOME ... !!!'
        self.assertEqual(observed, expected)

    def test_lower(self):
        observed = Task1.lower('People Are Awesome ... !!!')
        expected = 'people are awesome ... !!!'
        self.assertEqual(observed, expected)

    def test_split(self):
        observed = Task1.split('People Are Awesome ... !!!')
        expected = ['People', 'Are', 'Awesome', '...', '!!!']
        self.assertEqual(observed, expected)

    def test_strip(self):
        observed = Task1.strip('People Are Awesome ... !!!')
        expected = 'People Are Awesome '
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
