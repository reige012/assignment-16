#! /usr/bin/env python
# encoding UTF-8

'''
Assignment16Task2_test biol7800
ZacCarver 03/30/2016
'''

import datetime
#import pandas as pd
import unittest
import A16T2


class TestA16T2(unittest.TestCase):

    def test_num_entries(self):
        observed = A16T2.num_entries(['1', '2', '3'])
        expected = 3
        self.assertEqual(observed, expected)

    def test_date_l(self):
        #create a mock datetime
        '''beg = datetime.datetime.strptime(df['Date'].min(), "%Y-%m-%d")
        return beg'''

    def test_date_r(df):
        #create a mock datetime
        '''end = datetime.datetime.strptime(df['Date'].max(), "%Y-%m-%d")
        return end'''

    def test_since(r):
        #create a mock datetime
        '''now = datetime.date.today()
        years = now.year - r.year
        return years'''

    def test_fltr(df):
        #create mock csv data
        #http://stackoverflow.com/questions/5237693/mocking-openfile-name-in-unit-tests
        '''fun_hos = df.iloc[:, (1, 2)]
        return fun_hos'''

if __name__ == '__main__':
    unittest.main()
