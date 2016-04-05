#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 16 that tests a bunch of stuff.
 Helpful hints and collaboration provided by Mikey Henson, aka Pineapple House.
 Information and examples for pandas accessed from:
 http://pandas.pydata.org/pandas-docs/stable/tutorials.html
 http://www.swegler.com/becky/blog/2014/08/06/useful-pandas-snippets/

 Created by A.J. Turner on March 30, 2016.
"""
import pandas
import numpy


def sortme(otu_stuff):
    sort_otu = otu_stuff.sort_values(['FWC_2'], ascending=True)
    return sort_otu


def col_del(otu_stuff):
    delete = otu_stuff.drop('FWC_1', 1)
    return delete


def rep_value(otu_stuff):
    new_value = otu_stuff.replace(10, numpy.nan)  # replace 10 with NaN
    return new_value


def sumit(otu_stuff):
    mysum = otu_stuff['FWC_1'].sum(axis=0)  # sums values in column 2 (FWC_1)
    return mysum


def new_name(otu_stuff):
    '''changing name of column headers'''
    names = otu_stuff.rename(columns={'FWC_1': 'Site_1', 'FWC_2': 'Site_2'})
    return names


def main():
    otu_stuff = pandas.read_csv('test_file.csv')
    sort_otu = sortme(otu_stuff)
    print(sort_otu)
    delete = col_del(otu_stuff)
    print(delete)
    new_value = rep_value(otu_stuff)
    print(new_value)
    mysum = sumit(otu_stuff)
    print(mysum)
    names = new_name(otu_stuff)
    print(names)


if __name__ == '__main__':
    main()
