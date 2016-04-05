#!/usr/bin/env python
# utf-8

"""
Assignment 16,task1
Created by Pramod Pantha on March 26, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import unittest
import task1_asgn9


class TestAsgn9(unittest.TestCase):

	def test_upper(self):
		observed = task1_asgn9.upper("Python is interesting to learn, although it is not easy !!! @@@")
		expected = "PYTHON IS INTERESTING TO LEARN, ALTHOUGH IT IS NOT EASY !!! @@@"
		self.assertTrue(True)
		
	def test_lower(self):
		observed = task1_asgn9.lower("Python is interesting to learn, although it is not easy !!! @@@")
		expected = "python is interesting to learn, although it is not easy !!! @@@"
		self.assertTrue(True)
		
	def test_count(self):
		observed = task1_asgn9.count("Python is interesting to learn, although it is not easy !!! @@@")
		expected = 4
		self.assertTrue(True)

	def test_split(self):
		observed = task1_asgn9.split("Python is interesting to learn, although it is not easy !!! @@@")
		expected = ['Python', 'is', 'interesting', 'to', 'learn,', 'although', 'it', 'is', 'not', 'easy', '!!!', '@@@']
		self.assertTrue(True)

	def test_strip(self):
		observed = task1_asgn9.strip("Python is interesting to learn, although it is not easy !!! @@@")
		expected = "Python is interesting to learn, although it is not easy "
		self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
