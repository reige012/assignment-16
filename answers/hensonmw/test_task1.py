#!/usr/bin/env python
# encoding: utf-8

import unittest
import mwh_assin9task2

"""
My 1st testing program for Assignment 16 on assignment 9 test2
I worked with AJ dun dun dun
Created by Michael Henson on 30 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""


class TestAssign9(unittest.TestCase):
    def test_reformat_tree(self):
        observed = mwh_assin9task2.reformat_tree('''Microbes are cool\tDawgs Suck\nGo LSU\tThrash lab rules\n''')
        expected = ['Microbes are cool,Dawgs Suck','Go LSU,Thrash lab rules','']
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
