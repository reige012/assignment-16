#!/usr/bin/env python

"""
Task 1:
Here is a quote from Albert Einstein:

"The most beautiful thing we can experience is the mysterious. It is the source
 of all true art and science." This quote is also a string. Write a program
 that includes 5 different functions each of which demonstrates one of 5
 different string methods. As always, your program should contain a main loop
 and an ifmain statement.

Created by Shraddha Shrestha on February 24, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

 """
import unittest
import Task1


class TestTask1(unittest.TestCase):

    def test_count_quote(self):
        # To count the number of any letter in the following quote.
        observed = Task1.count_quote(quote)
        expected = 10
        self.assertEqual(observed, expected)

    def test_quote_upper(self):
        # To capitalize every letter in the quote.
        observed = Task1.quote_upper(quote)
        expected = "THE MOST BEAUTIFUL THING WE CAN EXPERIENCE IS THE MYSTERIOUS. IT IS THE SOURCE OF ALL TRUE ART AND SCIENCE."
        self.assertEqual(observed, expected)

    def test_quote_split(self):
        # To split the quote in its characters.
        observed = Task1.quote_split(quote)
        expected = ['The', 'most', 'beautiful', 'thing', 'we', 'can', 'experience', 'is', 'the', 'mysterious.', 'It', 'is', 'the', 'source', 'of', 'all', 'true', 'art', 'and', 'science.']
        self.assertEqual(observed, expected)

    def test_length_string(self):
        # Find the length of quote.
        observed = Task1.length_string(quote)
        expected = 107
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    quote = "The most beautiful thing we can experience is the mysterious. It\
 is the source of all true art and science."
    unittest.main()
