# !/usr/bin/env python
# encoding: utf-8


"""
My testing of assignment 14 task1 program
Created by Andre Moncrieff on 20 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import unittest
from collections import Counter
from a14task1 import WordCounter


class TestA14Task1(unittest.TestCase):
    def path(self):
        """
        To user/grader: paste in your path below for the task1 test files
        """
        return "/Users/Andre/Desktop/Comp_Prog_for_Biologists/assignment-16/answers/AndreMonc/task1_files/task1_test_files"

    def test_init_set_things_up_path(self):
        test_obj = WordCounter(self.path())
        observed = test_obj.dir_path
        expected = self.path()
        test_obj.close_files()
        self.assertEqual(observed, expected)

    def test_init_set_things_up_filenames(self):
        """
        This test is nearly redundant on the test below, but I wanted to do a
        test on my creation of attributes. Note that I do not test all my
        attributes in the init portion (because the attributes are based on
        the methods that I test below).
        """
        test_obj = WordCounter(self.path())
        observed = test_obj.list_of_filenames
        expected = ["test1.txt", "test2.txt"]
        test_obj.close_files()
        self.assertEqual(observed, expected)

    def test_list_of_filenames(self):
        test = WordCounter.list_of_filenames(WordCounter, self.path())
        observed = test
        expected = ["test1.txt", "test2.txt"]
        self.assertEqual(observed, expected)

    def test_cleaned_up_word_list(self):
        test = WordCounter(self.path())
        observed = test.word_list_1
        expected = ['one', 'andre', 'test', 'money', 'change', 'mister',
                    'whoop-yeah', 'diggity-doo', 'moncrieff', 'one']
        test.close_files()
        self.assertEqual(observed, expected)

    def test_word_count(self):
        observed = WordCounter.word_count(WordCounter,
                                          ['hey', 'I', 'am', 'a', 'beginning',
                                           'programmer'])
        expected = 6
        self.assertEqual(observed, expected)

    def test_set_of_list(self):
        the_list = ['one', 'andre', 'test', 'money',
                    'change', 'mister', 'whoop-yeah',
                    'diggity-doo', 'moncrieff', 'one']
        observed = WordCounter.set_of_list(WordCounter, the_list)
        expected = set(the_list)
        self.assertEqual(observed, expected)

    def test_count_and_dictionate(self):
        the_list = ['one', 'andre', 'test', 'money',
                    'change', 'mister', 'whoop-yeah',
                    'diggity-doo', 'moncrieff']
        observed = Counter(the_list)
        expected = WordCounter.count_and_dictionate(WordCounter, the_list)
        self.assertEqual(observed, expected)

    def test_intersection(self):
        set1 = {'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                'change', 'test', 'one', 'whoop-yeah'}
        set2 = {'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                'change', 'test', 'two', 'whoop-yeah'}
        observed = WordCounter.intersection(WordCounter, set1, set2)
        expected = len({'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                        'change', 'test', 'whoop-yeah'})
        self.assertEqual(observed, expected)

    def test_in_1_not_2(self):
        set1 = {'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                'change', 'test', 'one', 'whoop-yeah'}
        set2 = {'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                'change', 'test', 'two', 'whoop-yeah'}
        observed = WordCounter.in_1_not_2(WordCounter, set1, set2)
        expected = len({'one'})
        self.assertEqual(observed, expected)

    def test_in_2_not_1(self):
        set1 = {'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                'change', 'test', 'one', 'whoop-yeah'}
        set2 = {'andre', 'mister', 'money', 'diggity-doo', 'moncrieff',
                'change', 'test', 'two', 'whoop-yeah'}
        observed = WordCounter.in_2_not_1(WordCounter, set1, set2)
        expected = len({'two'})
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()
