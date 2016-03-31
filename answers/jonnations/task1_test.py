#!/usr/bin/env python
# utf-8


"""
This programm tests a modified Version of Assignment 10, Task 3. The new
version is Assignment 16 task1.py
by Jon Nations on 29 March 2016"""


import unittest
import task1


class TestTask1(unittest.TestCase):

    def test_code_dic(self):
        observed = task1.code_dic('ExaML_info.T5\tLikelihood of best tree:\t-82924194.71')
        expected = {'ExaML_info.T5': '-82924194.71'}
        self.assertEqual(observed, expected)

    def test_best(self):
        observed = task1.best({'A': 3, 'B': 2, 'C': 1})
        expected = [('C', 1)]
        self.assertEqual(observed, expected)

if __name__ == '__main__':
    unittest.main()
