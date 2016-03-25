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


def lists_c_name(file):
    """
    takes input .csv file and splits on commas
    returns list of lists, pertaining to rows in file
    starting at common name and including only the data
    """
    my_lists = []
    for line in file:
        l = line.split(',')
        my_lists.append(l[6:])
    return my_lists


def array(my_list):
    """convert list to numpy array"""
    array = np.array(my_list)
    return array


def data_frame(array, l):
    """takes array or list and converts ot pandas dataframe"""
    data_frame = DataFrame(array, columns = l)
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
    l_cname = lists_c_name(my_file)
    l = l_cname.pop(0)
    df = data_frame(l_cname, l)
    # add index by common name
    df.index = df['common_name']
    df.pop('common_name')
    families = get_family(my_array)
    species = get_species(DataFrame(my_array))
    pear = pearson_coof(my_array, 10, 16)
    print("the correlation coefficient of adult mass and egg mass is: {}".format(pear))

if __name__ == '__main__':
    main()
