#!/usr/bin/env python
# encoding: utf-8
"""
create by me to use unittest to test my function from task2 assignment 9
"""
import unittest
import task2_9


class Testtask2(unittest.TestCase):

    def test_replace(self):
        observed = task2_9.replace('1\t2\t')
        expected = '1,2,'
        self.assertEqual(observed, expected)

    def test_split(self):
        observed = task2_9.split('flower\n\nspring\n')
        expected = ['flower', '', 'spring', '']
        self.assertEqual(observed, expected)

    def test_remove(self):
        observed = task2_9.remove(['flower', '', 'spring', ''])
        expected = ['flower', 'spring']
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
