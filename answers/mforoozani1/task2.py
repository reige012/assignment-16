#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to do some common excell task
"""
import csv


def read_data(filename):
    with open(filename, 'r') as f:
        parsed_data = [row for row in csv.reader(f.read().splitlines())]
    return parsed_data


def read_header(A):
    B = A[0]
    return B


def find_geneId(C):
    D = C[1][0]
    return D


def str_inte(E):
    F = E[1][1::]
    G = [int(i) for i in F]
    return G


def sum_count_replicates(H):
    return sum(H)


def main():
    df = read_data('test.csv')
    print(df)
    header = read_header(df)
    print(header)
    geneId = find_geneId(df)
    print(geneId)
    result = str_inte(df)
    print(result)
    sumcount = sum_count_replicates(result)
    print(sumcount)

if __name__ == '__main__':
    main()
