#!/usr/bin/env python
# encoding: utf-8
"""
create by me to use unittest to test my function from task2 assignment 9
"""
import unittest
import task2


class Testtask2(unittest.TestCase):

    def test_read_data(self):
        observed = task2.read_data('test.csv')
        expected = [['geneID', 'WTC1', 'WTC2', 'WTC3'],
                    ['Os01g01010', '1656', '1853', '1204'],
                    ['Os01g01019', '35', '20', '5']]
        self.assertEqual(observed, expected)

    def test_read_header(self):
        observed = task2.read_header([['geneID', 'WTC1', 'WTC2', 'WTC3'],
                                      ['Os01g01010', '1656', '1853', '1204'],
                                      ['Os01g01019', '35', '20', '5']])
        expected = ['geneID', 'WTC1', 'WTC2', 'WTC3']
        self.assertEqual(observed, expected)

    def test_find_geneId(self):
        observed = task2.find_geneId([['geneID', 'WTC1', 'WTC2', 'WTC3'],
                                      ['Os01g01010', '1656', '1853', '1204'],
                                      ['Os01g01019', '35', '20', '5']])
        expected = 'Os01g01010'
        self.assertEqual(observed, expected)

    def test_str_inte(self):
        observed = task2.str_inte([['geneID', 'WTC1', 'WTC2', 'WTC3'],
                                   ['Os01g01010', '1656', '1853', '1204'],
                                   ['Os01g01019', '35', '20', '5']])
        expected = [1656, 1853, 1204]
        self.assertEqual(observed, expected)

    def test_sum_count_replicate(self):
        observed = task2.sum_count_replicates([1656, 1853, 1204])
        expected = 4713
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
