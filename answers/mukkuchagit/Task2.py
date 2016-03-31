#!/usr/bin/env python
# encoding: utf-8
"""
assignment 16.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import csv
from collections import defaultdict


def get_organism_with_body_mass(column, bm):
    index = list()
    for i in range(len(column)):
        if bm == float(column[i]):
            index.append(i)
    return index


def get_organism_with_longevity_morethan(column, long_y):
    index = []
    for i in range(len(column)):
        if long_y <= float(column[i]):
            index.append(i)
    return index


def find_unique_classes(column):
    unique_class = set(column)
    return unique_class


def count_no_of_species(column):
    species = len(column)
    return species


def count_no_of_genus(column):
    genus = set(column)
    return len(genus)


def import_columns(filename):
    columns = defaultdict(list)
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)
    return columns


def main():
    columns = import_columns('sub_table.csv')
    print(get_organism_with_body_mass(columns['adult_body_mass_g'], bm=114))
    print(get_organism_with_longevity_morethan(columns['longevity_y'], long_y=150))
    print(find_unique_classes(columns['class']))
    print(count_no_of_species(columns['species']))
    print(count_no_of_genus(columns['genus']))


if __name__ == '__main__':
    main()
