#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 9 Task 3

Amie Settlecowski
31 Mar. 2016

This program is a unit test for Assignment 9 Task 3.
"""
import argparse


def input_list():
    # parses user input and returns phrase to main
    # source: https://youtu.be/rnatu3xxVQE
    parser = argparse.ArgumentParser()
    parser.add_argument("--list",
                        required=True,
                        nargs='+',
                        type=int,
                        help="Enter a list of intergers separated by spaces")
    args = parser.parse_args()
    return args


def odd_even(x):
    # takes integer x and returns 0 when x is 0 or even and 1 when x is odd
    return x % 2


def remove_even(l):
    odd_l = []
    for n in l:
        if odd_even(n) != 0:
            odd_l.append(n)
        else:
            pass
    return odd_l


def main():
    l = input_list()
    l_odd = remove_even(l.list)
    print(l_odd)

if __name__ == '__main__':
    main()
