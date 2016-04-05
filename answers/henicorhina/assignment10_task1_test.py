# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 16
Oscar Johnson 28 February 2016
"""

import unittest

import assignment10_task1


class TestAssignment10(unittest.TestCase):

    def test_quote_dict(self):
        observed = assignment10_task1.quote_dict("word words word's")
        expected = ({'word': 0, 'words': 0}, ['word', 'words', 'words'])
        self.assertEqual(observed, expected)

    def test_word_counter(self):
        observed = assignment10_task1.word_counter({'word': 0, 'words': 0},
                                                   ['word', 'words', 'words'])
        self.assertEqual(observed, [(2, 'words'), (1, 'word')])


if __name__ == '__main__':
    unittest.main()
