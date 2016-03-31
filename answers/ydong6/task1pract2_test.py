#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 22, 2016
Task 1

Starting with assignment-9 (or any later assignment), pick the code from one of
the tasks that you wrote and write a set of unit tests that test each function
in your program. You may need to slightly refactor your older code to work with
your units tests (although you shouldn't have to change very much). Be sure to
use unittest and include a unittest.main() call in your ifmain loop. Also be
sure to format your code correctly. 
@author: York
'''
import unittest
import task1pract2

class Task1pract2(unittest.TestCase):
  
    def test_upper(self):
        observed=task1pract2.upper('The')
        expected='THE'
        self.assertEqual(observed,expected)
        
        
    def test_split(self):
        observed=task1pract2.split('super cold')
        expected=['super','cold']
        self.assertEqual(observed,expected)
        
        
    def test_times(self):
        observed=task1pract2.times('he is is')
        expected=2
        self.assertEqual(observed,expected)

    
    def test_find(self):
        observed=task1pract2.find('The most beautiful thing we can experience is the mysterious. It is the source of all true art and science.')
        expected=25
        self.assertEqual(observed,expected)
        
        
    def test_lower(self):
        observed=task1pract2.lower('Super cold')
        expected=('super cold')
        self.assertEqual(observed,expected)

    
if __name__ == '__main__':
    unittest.main()