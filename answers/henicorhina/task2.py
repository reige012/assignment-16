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

import matplotlib.pyplot as plt
import numpy as np
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


def lists_df(file):
    """
    takes input .csv file and splits on commas
    returns list of lists, pertaining to rows in file
    also returns index and column values for pandas DataFrame    
    """
    my_lists = []
    index = []
    for line in file:
        line.strip('\n')
        l = line.split(',')
        my_lists.append(l[7:])
        index.append(l[6])
    cols = my_lists.pop(0)
    return my_lists, index, cols


def array(my_list):
    """convert list to numpy array"""
    array = np.array(my_list)
    return array


def frame(array):
    """takes array or list and converts ot pandas dataframe"""
    data_frame = DataFrame(array)
    return data_frame


def get_family(array):
    """
    takes numpy array and returns a list of the family names in the database
    """
    f = array[:, 2]
    l = list(f)
    s = set(l)
    # print(s)
    return s


def get_species(data_frame):
    """
    takes pandas DataFrame and returns a set of the species in the database
    """
    combined = data_frame[3] + "_" + data_frame[4]
    l = list(combined)
    s = set(l)
    # print(s)
    return s


def pearson_coof(array, col1, col2):
    """
    takes an array and which columns you wish to correlate
    returns the pearson product-moment correlation coefficient
    """
    x = array[1:, col1]
    y = array[1:, col2]
    value = np.corrcoef(x, y, rowvar=0)
    return value
    return x, y


def main():
    my_file = open('Aves_Database_Aug_2015.csv', 'r')
    lists = listify(my_file)
    my_array = array(lists)
    frame(my_array)
    l_cname = lists_df(my_file)
    my_file.close()
    # add index by common name
    families = get_family(my_array)
    species = get_species(DataFrame(my_array))
    pear = pearson_coof(my_array, 10, 16)
    print("the correlation coefficient of adult mass and egg mass is: {}".format(pear))
    # convert to DataFrame with appropriate indices columns
    data_frame = DataFrame(l_cname[0], index=l_cname[1][1:], columns=l_cname[2])

if __name__ == '__main__':
    main()
