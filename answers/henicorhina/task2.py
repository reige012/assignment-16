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

import numpy as np
import pdb
from pandas import DataFrame


def listify(file):
    """
    takes input .csv file and splits on commas
    returns list of lists, pertaining to rows in file
    """
    my_lists = []
    for line in file:
        l = line.split(',')
        my_lists.append(l)
    return my_lists


def lists_df(mfile):
    """
    takes input .csv file and splits on commas
    returns list of lists, pertaining to rows in file
    also returns index and column values for pandas DataFrame
    """
    my_lists = []
    index = []
    for line in mfile:
        line.strip('\n')
        line.replace('-999', '0')
        l = line.split(',')
        my_lists.append(l[7:])
        index.append(l[6])
    new_line = []
    for lines in my_lists[1:]:
        li = []
        for val in lines[0:]:
            li.append(float(val))
        new_line.append(li)
    # pdb.set_trace()
    cols = my_lists[0]
    return new_line, index, cols


def array(my_list):
    """convert list to numpy array"""
    array = np.array(my_list)
    return array


def frame(array, i, c):
    """
    takes array or list and converts to pandas dataframe
    i = index of rows, c = columns
    """
    data_frame = DataFrame(array, index=i, columns=c)
    return data_frame


def get_family(array):
    """
    takes numpy array and returns a list of the family names in the database
    """
    f = array[:, 2]
    l = list(f)
    s = set(l)
    # pdb.set_trace()
    return s


def get_species(data_frame):
    """
    takes pandas DataFrame and returns a set of the species in the database
    """
    combined = data_frame[3] + "_" + data_frame[4]
    l = list(combined)
    s = set(l)
    # pdb.set_trace()
    return s


def pearson_cooef(x, y):
    """
    takes two columns of an array that you wish to correlate
    returns the pearson product-moment correlation coefficient as an array
    """
    value = np.corrcoef(x, y, rowvar=1)
    return value


def main():
    with open('Aves_Database_Aug_2015.csv', 'r') as my_file:
        l_cname = lists_df(my_file)
        # pdb.set_trace()
        l_1 = l_cname[1][1:]  # corrects a minor error in lists_df
        df = frame(l_cname[0], l_1, l_cname[2])
        pear = pearson_cooef(df.egg_mass_g, df.adult_body_mass_g)
        print("""the correlation coefficient of adult mass and egg mass is:
        {}""".format(pear[0][1]))
    with open('Aves_Database_Aug_2015.csv', 'r') as my_file2:
        lists = listify(my_file2)
        my_array = array(lists)
        families = get_family(my_array)
        species = get_species(DataFrame(my_array))
        print("""your dataset includes:
        {} families
        and {} species""".format(len(families), len(species)))

if __name__ == '__main__':
    main()
