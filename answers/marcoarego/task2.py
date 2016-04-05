# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marco
# @Date:   2016-03-27 15:36:54
# @Last Modified by:   Marco
# @Last Modified time: 2016-03-30 16:15:27


import unittest
import task2_code


class TestTask2(unittest.TestCase):
    """docstring for TestTask2"""
    def test1_unique_fields_count(self):
        for x in [1, 2, 3]:
            if x == 1:
                observed = task2_code.unique_fields_count([['l1', 'l2', 'l3'],
                                                          ['a', 'b', 'd'],
                                                          ['a', 'e', 'f']],
                                                          0)
                expected = 1
                self.assertEqual(observed, expected)
            elif x == 2:
                observed = task2_code.unique_fields_count([['l1', 'l2', 'l3'],
                                                          ['a', 'b', 'd'],
                                                          ['a', 'e', 'f']],
                                                          1)
                expected = 2
                self.assertEqual(observed, expected)
            elif x == 3:
                observed = task2_code.unique_fields_count([['l1', 'l2', 'l3'],
                                                          ['a', 'b', 'd'],
                                                          ['a', 'e', 'f']],
                                                          2)
                expected = 2
                self.assertEqual(observed, expected)

    def test2_text2dict(self):
        observed = task2_code.text2dict([['l1', 'l2', 'l3'],
                                        ['a', 'b', 'd'],
                                        ['a', 'e', 'f']], 0, 1)
        expected = ({'l1': ['l2'], 'a': ['b', 'e']})
        self.assertEqual(observed, expected)

    def test3_clean_dict(self):
        observed = task2_code.clean_dict({'l1': ['l2', 'l4'],
                                         'a': ['b', 'b', 'e']})
        expected = {'a': {'b', 'e'}, 'l1': {'l2', 'l4'}}
        self.assertEqual(observed, expected)

    def test4_taxon_by_group(self):
        observed = task2_code.taxon_by_group({'l1': ['l2', 'l4'],
                                             'a': ['a', 'b', 'e']})
        expected = {'l1': 2, 'a': 3}
        self.assertEqual(observed, expected)

    def test5_percent(self):
        observed = task2_code.percent({'l1': 3, 'a': 3})
        expected = {'l1': '50.0%', 'a': '50.0%'}
        self.assertEqual(observed, expected)

if __name__ == '__main__':
    unittest.main()
