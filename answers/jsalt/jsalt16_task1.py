#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 16
Task 1 Program: Unittests for Assignment 11 Task 2
Jessie Salter
27 March 2016
"""

import unittest
import jsalt11_task2
import os


class Test_jsalt11_task2(unittest.TestCase):

    def test_prompt(self):
        observed = jsalt11_task2.prompt(['--input', 'test.txt'])
        expected = 'test.txt'
        self.assertEqual(observed.input, expected)

    def test_t_words(self):
        observed = jsalt11_task2.t_words('test.txt')
        expected = ['this\t1\n', 'test\t1\n']
        self.assertEqual(observed, expected)

    def test_output_path(self):
        observed = jsalt11_task2.output_path('test.txt')
        expected = 'T-words-test.txt'
        self.assertEqual(observed, expected)

    def test_results_file(self):
        # I'm not sure if this is really a robust test, or I'm feeding it all
        # the necessary info to pass...will need to give this another look.
        jsalt11_task2.results_file(
            ['this\t1\n', 'test\t1\n'],
            'T-words-test.txt'
            )
        # Tests whether a file exists with the expected name:
        self.assertTrue(os.path.isfile('T-words-test.txt'))
        obs_filepath = os.path.abspath('T-words-test.txt')
        ex_filepath = '/Users/jsalt/Desktop/assignment-16/answers/jsalt/T-words-test.txt'
        self.assertEqual(obs_filepath, ex_filepath)


if __name__ == '__main__':
    unittest.main()
