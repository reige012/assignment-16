#!/usr/bin/env python
# encoding: utf-8

import pandas

"""
My 2nd task for assignment 16
I worked with AJ dun dun dun
Created by Michael Henson on 30 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""


def sorting(files):
    sort = files.sort_values(['Swamp_A'], ascending=False)
    return sort


def transpose(sort):
    transposed = sort.T
    return transposed


def deleting_columns(sort):
    x = sort.drop('Swamp_B', 1)
    return x


def evaluation(delete):
    x = len(delete[(delete['Swamp_A'] > 10)])
    return x


def mean(df):
    df['mean'] = df.mean(axis=1)
    return df


def main():
    df = pandas.read_csv("Swamp_tests.csv", header=0, index_col=0)
    sort = sorting(df)
    print("Here is your sorted OTU table\n")
    print(sort)
    transposed = transpose(sort)
    print("\nHere is your sorted OTU table now transposed\n")
    print(transposed)
    delete = deleting_columns(sort)
    print("\nLets remove a column because maybe it was contaminated")
    print(delete)
    evalulations = evaluation(delete)
    print("\nThere are {} OTUs with more than 10 reads".format(evalulations))
    means = mean(df)
    print("\nSometimes we want to know the mean of our data\n")
    print(means)


if __name__ == '__main__':
    main()
