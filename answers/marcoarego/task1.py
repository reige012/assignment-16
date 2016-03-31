# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-03-27 14:30:36
# @Last Modified by:   Marco
# @Last Modified time: 2016-03-27 15:35:22


import unittest
import task1_Assign10


class TestAss10(unittest.TestCase):

    def test1_string_standizer(self):
        observed = task1_Assign10.string_standizer("My,'+ StRinG!\n")
        expected = "my string"
        self.assertEqual(observed, expected)

    def test2_word_counter(self):
        observed = task1_Assign10.word_counter("my my this string is beautiful")
        expected = {'my': 2, 'this': 1, 'string': 1, 'is': 1, 'beautiful': 1}
        self.assertEqual(observed, expected)

    def test3_dict_reversor(self):
        observed = task1_Assign10.dict_reversor(
         {'my': 2, 'this': 1, 'string': 1, 'is': 1, 'beautiful': 1})
        expected = sorted([(2, 'my'), (1, 'this'), (1, 'string'),
                          (1, 'is'), (1, 'beautiful')])
        self.assertEqual(observed, expected)

    def test4_get_more_common_words(self):
        s = [(1, 'this'), (2, 'my'), (1, 'string'), (1, 'is'), (1, 'beautiful')]
        observed = task1_Assign10.get_more_common_words(s, 1)
        expected = [(2, 'my')]
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
