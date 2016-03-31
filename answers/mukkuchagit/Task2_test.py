#!/usr/bin/env python
# encoding: utf-8
"""
assignment 16.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import unittest
import Task2


class TestTask2(unittest.TestCase):

    def test_get_organism_with_body_mass(self):
        columns = Task2.import_columns('sub_table.csv')
        observed = Task2.get_organism_with_body_mass(columns['adult_body_mass_g'], bm=114)
        self.assertEqual(observed, [1342, 1645, 4309, 7329])

    def test_get_organism_with_longevity_morethan(self):
        columns = Task2.import_columns('sub_table.csv')
        observed = Task2.get_organism_with_longevity_morethan(columns['longevity_y'], long_y=150)
        self.assertEqual(observed, [21255, 21265])

    def test_find_unique_classes(self):
        columns = Task2.import_columns('sub_table.csv')
        observed = Task2.find_unique_classes(columns['class'])
        self.assertEqual(observed, {'Mammalia', 'Reptilia', 'Aves'})

    def test_count_no_of_species(self):
        columns = Task2.import_columns('sub_table.csv')
        observed = Task2.count_no_of_species(columns['species'])
        self.assertEqual(observed, 21322)

    def test_count_no_of_genus(self):
        columns = Task2.import_columns('sub_table.csv')
        observed = Task2.count_no_of_genus(columns['genus'])
        self.assertEqual(observed, 4336)


if __name__ == '__main__':
    unittest.main()
