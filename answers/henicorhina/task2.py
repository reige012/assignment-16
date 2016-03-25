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


def array(my_list):
    """convert list to numpy array"""
    array = np.array(my_list)
    return array


def data_frame(array):
    """takes array and converts ot pandas dataframe"""
    data_frame = DataFrame(array)
    return data_frame


def get_family(array):
    """
    takes numpy array and returns a list of the family names in the database
    """
    f = array[:,2]
    l = list(f)
    s = set(l)
    # print(s)
    return s


def get_species(data_frame):
    """
    takes pandas DataFrame and returns a list of the species in the database    
    """
    combined = data_frame[3] + "_" + data_frame[4]
    l = list(combined)
    s = set(l)
    # print(s)
    return s


def main():
    my_file = open('/Users/home/Biol7800/assignment-16/answers/henicorhina/Aves_Database_Aug_2015.csv', 'r')
    lists = listify(my_file)
    my_array = array(lists)
    df = data_frame(my_array)
    families = get_family(my_array)
    species = get_species(df)


if __name__ == '__main__':
    main()
