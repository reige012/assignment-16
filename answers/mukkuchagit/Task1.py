#!/usr/bin/env python
# encoding: utf-8
"""
assignment 16.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""


def count(arg):
    x = arg.count('e')
    return x


def upper(arg):
    i = arg.upper()
    return i


def lower(arg):
    j = arg.lower()
    return j


def split(arg):
    y = arg.split(' ')
    return y


def strip(arg):
    z = arg.strip('!').strip(' ').strip('.')
    return z


def main():
    arg = "People Are Awesome ... !!!"
    a = count(arg)
    print('count method: ', a)
    b = upper(arg)
    print("upper method: ", b)
    c = lower(arg)
    print('lower method: ', c)
    d = split(arg)
    print('split method: ', d)
    e = strip(arg)
    print('strip method: ', e)


if __name__ == '__main__':
    main()
