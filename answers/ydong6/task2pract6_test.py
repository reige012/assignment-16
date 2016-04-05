#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 23, 2016
Task 2

Write a program that does something you need (or want) for it to do. The program
can do anything, but it should have between 5 and 10 functions (or more, if you
really want). You should also write a separate set of unit tests for your
program to test that each function is performing as you would expect. You may
use any sort of input data you like (your own, someone elses, etc.). If you want
some data you could do stuff with, there are many sources online... one of my
recent favorites is this set of natural history traits of different organisms.

Be sure to trim your input data file to a reasonable size before committing it
to your repository (git does not like to store large, unchanging, files). Please
also include, in a README.md file in your repository, a description of what your
program does and how to use it. @author: York
'''
import unittest
import task2pract6


class Task2prac6(unittest.TestCase):


    def test_clean(self):
        observed=task2pract6.clean('The')
        expected='the'
        self.assertEqual(observed,expected)
    
    def test_comb(self):
        observed=task2pract6.comb('adads')
        expected='a d a d s'
        self.assertEqual(observed,expected)
    
    def test_times(self):
        observed=task2pract6.times('accads')
        expected=2
        self.assertEqual(observed,expected)
    
    def test_find(self):
        observed=task2pract6.find('adcttads')
        expected=3
        self.assertEqual(observed,expected)
    
    def test_replace(self):
        observed=task2pract6.replace('adnnads')
        expected='adaaads'
        self.assertEqual(observed,expected)
    
    def test_makelist(self):
        observed=task2pract6.makelist('ad')
        expected=['[', "'", 'a', 'd', "'", ']'] 
        self.assertEqual(observed,expected)
    

if __name__ == "__main__":
    unittest.main()