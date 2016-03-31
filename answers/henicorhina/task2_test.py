# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 16
Oscar Johnson 24 March 2016

Copyright Oscar Johnson 2016

Analysis of avian life history data using the database
compiled by Myhrvold et al. 2015:

Nathan P. Myhrvold, Elita Baldridge, Benjamin Chan, Dhileep Sivam, Daniel L.
Freeman, and S. K. Morgan Ernest. 2015. An amniote life-history database to
perform comparative analyses with birds, mammals, and reptiles. Ecology
96:3109. http://dx.doi.org/10.1890/15-0846.1
"""

import unittest
import numpy
import pandas

import task2


class TestTask2(unittest.TestCase):

    def test_listify(self):
        """ test that data type is correct"""
        observed = task2.listify('name, item \n name2, item2')
        self.addTypeEqualityFunc(list, observed)

    def test_lists_df_1(self):
        """test that data type is correct"""
        my_file = open('Aves_Database_Aug_2015.csv', 'r')
        observed = task2.lists_df(my_file)
        self.addTypeEqualityFunc(list, observed[0])

    def test_lists_df_2(self):
        """test that list contains some data"""
        my_file = open('Aves_Database_Aug_2015.csv', 'r')
        obs = task2.lists_df(my_file)
        observed = obs[0][0]
        self.addTypeEqualityFunc(str, observed)

    def test_array(self):
        """ test that data type is correct"""
        observed = task2.array([['name, item'], ['name2, item2']])
        self.addTypeEqualityFunc(numpy.ndarray, observed)

    def test_frame1(self):
        """ test that data type is correct"""
        observed = task2.frame(numpy.array([['name', 'item'],
                                            ['name2', 'item2'],
                                            ['name3', 'item3']]),
                               i=['1', '2', '3'],
                               c=['1', '2'],)
        self.addTypeEqualityFunc(pandas.core.frame.DataFrame, observed)

    def test_frame2(self):
        """
        test that length is correct
        'length' is the length of the index
        """
        obs = task2.frame(numpy.array([['name', 'item'],
                                      ['name2', 'item2'],
                                      ['name3', 'item3']]),
                          i=['1', '2', '3'],
                          c=['1', '2'],)
        observed = len(obs)
        self.assertEqual(observed, 3)

    def test_get_family(self):
        """test that I'm getting correct families in array"""
        my_file = open('Aves_Database_Aug_2015.csv', 'r')
        l = task2.listify(my_file)
        my_file.close()
        x = task2.array(l)
        observed = task2.get_family(x)
        self.assertIn('Accipitridae', observed)

    def test_get_species(self):
        """test that I'm getting correct species names in array"""
        my_file = open('Aves_Database_Aug_2015.csv', 'r')
        l = task2.listify(my_file)
        my_file.close()
        a = pandas.DataFrame(numpy.array(l))
        observed = task2.get_species(a)
        self.assertIn('Mimus_gilvus', observed)

    def test_pearson_coof(self):
        """
        """
        pass

if __name__ == '__main__':
    unittest.main()
