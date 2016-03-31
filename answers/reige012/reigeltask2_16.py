#!/usr/bin/env python
# encoding: utf-8

"""
Program completes several tasks necessary to parse the microsatellite data from
my Master's thesis work.

The output for this program is six separate files. Three containing the alleles
associated with each population and then a file for each popluation with their
alleles as sets.

Edited by Alicia Reigel. 25 March 2016.
Copyright Alicia Reigel. Louisiana State University. 25 March 2016. All
rights reserved.

"""


import argparse
import os
import re
import sys


def parser_filepath(args):
    """Collects the full path to the file you want to work with"""
    parser = argparse.ArgumentParser(
        description="""Input the full path to the file of interest"""
        )
    parser.add_argument(
            '--filepath',
            required=True,
            type=str,
            help='Enter the full path to the file of interest.'
        )
    return parser.parse_args(args)


def clean_file(file):
    cleaned_data = file.replace(',', '')
    return cleaned_data


def individuals_list(a_string):
    """creates a list for each line in the file and splits each allele counter
           into a new list value"""
    for line in a_string:
        lines = a_string.splitlines()
        # splits each line into a list entry
    counter = 0
    for x in lines:
        lines[counter] = x.split('\t')
        # splits each item separated by a tab into a new list entry
        counter += 1
    return lines


def make_individ_dict(some_list):
    """makes a dictionary with each population as a key and each allele data
        point as a value for that key"""
    individ_dict = {}
    for line in some_list:
        if line[0] in individ_dict:
            # append the new number to the existing array at this slot
            individ_dict[line[0]].append(line[1:27])
        else:
            # create a new array in this slot
            individ_dict[line[0]] = [line[1:27]]
    return individ_dict


def make_values_one_list(a_dict):
    """combines multiple value lists into one list of values for each key"""
    new_dict = {k: list({x for t in v for x in t if x != k}) for k, v in a_dict.items()}
    return new_dict


def print_entries_to_file(a_dict):
    """adds each dictionary entry into a new output file named for the key
        and creates a set that is added to a separate output file"""
    for k, v in a_dict.items():
        new_output_file = os.path.join(k + "_output")
        with open(new_output_file, 'w') as the_final_file:
            the_final_file.write("{}".format(v))
        with open(new_output_file, 'r') as input_data:
            a_string = input_data.read()
            clean_string = a_string.replace("'", '').replace(',', '').replace('[', '').replace(']', '').replace("  ", ' ').replace('\W*',' ').replace(':', '').replace("   ", '')
            # replaces unnecessary junk
            the_new_list = re.split(' ', clean_string)
            # splits on spaces to make a list of words
            the_set = set(the_new_list)
            print("The number of unique alleles in this set is {}.".format(len(the_set)))
            print(the_set)
            new_set = str(the_set)
            final_output_file = os.path.join(k+ "_set_output")
        with open(final_output_file, 'w') as set_data:
            set_data.write(new_set)


def main():
    args = parser_filepath(sys.argv[1:])
    with open(args.filepath, 'r') as input_file:
        data = input_file.read()
    cleaned_data = clean_file(data)
    list_of_individuals = individuals_list(cleaned_data)
    dict_of_individs = make_individ_dict(list_of_individuals)
    new_dict = make_values_one_list(dict_of_individs)
    print_entries_to_file(new_dict)


if __name__ == '__main__':
    main()
