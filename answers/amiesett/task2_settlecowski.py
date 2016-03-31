#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 16 Task 2

Amie Settlecowski
31 Mar. 2016

This program parses a csv file of life history traits for the taxonomic family
specified and summarizes data by genus.
"""
import argparse
import os

from collections import Counter

def get_args(parserr):
    '''
    Requires --i flag for user to indicate path to input file
    requires --o flag for user to name output file
    requires --family flag for user to specify taxanomic family
    '''
    parserr.add_argument("--i",
        required=True,
        help="Path to input file",
        type=str)

    parserr.add_argument("--o",
        required=True,
        help="Name for output file",
        type=str)

    parserr.add_argument("--family",
        required=True,
        help="Name of family in input .csv file to be analyzed",
        type=str)


def find_family(f, family):
    '''Retain data only from family of interest'''
    only_family = []
    for line in f:
        line = line.strip().split(',')
        if line[2] == family:
            reduced_line = []
            for index in [0, 1, 2, 3, 4, 6, 10, 22, 23]:
                reduced_line.append(line[index])
            line_as_tuple = tuple(reduced_line)
            only_family.append(line_as_tuple)
    return only_family


def count_genera(family_tup):
    '''Summarize species counts and weight data by genus'''
    genera_list = []
    all_weight = {}
    f_weight = {}
    m_weight = {}
    for index in family_tup:
        genus = index[3]
        al = index[6]
        female = index[7]
        male = index[8]
        genera_list.append(genus)
        build_dict(all_weight, genus, al)
        build_dict(f_weight, genus, female)
        build_dict(m_weight, genus, male)
    spp_counter = Counter()
    for genus in genera_list:
            spp_counter[genus] += 1
    return all_weight, f_weight, m_weight, spp_counter


def build_dict(dic, k, v):
    '''Adds data to appropriate genus in specified trait dictionary'''
    if k not in dic:
        dic[k] = [v]
    else:
        dic[k].append(v)


def to_file(out_f, counts):
    '''Write species counts per genus out file'''
    with open(out_f, 'w') as f:
        keys = counts.keys()
        for k in keys:
            f.write('{},{}\n'.format(k, str(counts[k])))


def main():
    # create Parser object with arguments for files and taxanomic family
    parser = argparse.ArgumentParser()
    get_args(parser)
    args = parser.parse_args()
    # change directory to that of input file
    working_dir = os.path.split(args.i)[0]
    os.chdir(working_dir)

    # parse input file for family of interest
    with open(args.i, 'r') as in_file:
        family = find_family(in_file, args.family)

    # summarize data by genus
    family_by_genus = count_genera(family)
    all_weight = family_by_genus[0]
    f_weight = family_by_genus[1]
    m_weight = family_by_genus[2]
    spp_counts = family_by_genus[3]

    # print output .csv file
    to_file(args.o, spp_counts)

if __name__ == '__main__':
    main()
