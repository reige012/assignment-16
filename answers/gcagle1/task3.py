#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
1 March 2016
Assignment 11 Task 3

A program taking a file as input and returning separate files containing all
the words starting with each letter of the alphabet, and their counts. The
first letter of the word is appended to the front of the file name.
'''
import argparse
import string
from collections import Counter
import os
# from pprint import pprint
# import json this might put the histogram tuple into a file...


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--infile",
        required=True,
        help="""The input file name"""
    )
    return parser.parse_args()


def remove_punct(args):
    exclude = set(string.punctuation)
    with open(args.infile, 'r') as f:
        my_input = f.read()
        remove_ch = ''.join(ch for ch in my_input if ch not in exclude)
        replace_data = remove_ch.lower().replace('\n', ' ')
        split_data = replace_data.split(' ')
        return(split_data)


def write_file(args, histogram, letters):
    d = histogram
    for letter in letters:
        myfile = ''.join("{}-{}".format(letter, os.path.basename(args.infile)))
        mydirectory = os.path.split(args.infile)[0]
        new_name = os.path.join(mydirectory, myfile)
        with open(new_name, 'w') as my_output:
            for word, value in iter(sorted(d.items(), key=lambda t: t[1],
            reverse=True)):
                if word.startswith(letter):
                    my_output.write("{0:15}{1}\n".format(word, value))


def main():
    letters = list(string.ascii_lowercase)
    args = get_args()
    histogram = dict(Counter(remove_punct(args)))
    remove_punct(args)
    write_file(args, histogram, letters)


if __name__ == '__main__':
    main()
