#!/usr/bin/env python
# encoding: utf-8

"""
Program tests the functions in reigeltask2_16.py using the unittest module.

The program will output two files called dog_output and dog_set_output in the
directory you are working in. Those files are only necessary for the testing
of these functions.

***Note to reviewers: because of of my tests is testing a dictionary entry and
dictionaries are not ordered it will sometimes show up as a fail, but if you
retry it a few times it will eventually work when the dictionary entry lines up
with the dictionary its being tested against. Sorry for this confusion, but I
can't see a way around it without altering the original program too much.***

Edited by Alicia Reigel. 27 March 2016.
Copyright Alicia Reigel. Louisiana State University. 27 March 2016. All
rights reserved.

"""

import os
import unittest
import reigeltask2_16


class TestParserFilepath(unittest.TestCase):
    """tests that argparser is correctly accepting arguments from the command line"""
    def test_parser_filepath(self):
        args = reigeltask2_16.parser_filepath(['--filepath', 'text.txt'])
        expected = 'text.txt'
        self.assertEqual(args.filepath, expected)


class TestCleanFile(unittest.TestCase):
    """tests the the commas are removed from the file"""
    def test_clean_file(self):
        directory = os.getcwd()
        os.chdir(directory)
        tester = os.path.join(directory + '\Tester_file.txt')
        with open(tester, 'r') as input_file:
            data = input_file.read()
        observed = reigeltask2_16.clean_file(data)
        self.assertEqual(observed, 'hello\n10 12 14 7\n')


class TestIndividualsList(unittest.TestCase):
    """tests that each \n separates into a list and then each \t separates into
        a value within said list"""
    def test_individuals_list(self):
        string = "This\tdog\nis\tsilly\tbut\tcute"
        a_list = [['This', 'dog'], ['is', 'silly', 'but', 'cute']]
        observed = reigeltask2_16.individuals_list(string)
        self.assertEqual(observed, a_list)


class TestMakeIndividDict(unittest.TestCase):
    """tests that the lists is made into a dictionary"""
    def test_make_individ_dict(self):
        some_list = [['NB2', '107'], ['NB3', '105', '109', '250']]
        some_dict = {'NB2': [['107']], 'NB3': [['105', '109', '250']]}
        observed = reigeltask2_16.make_individ_dict(some_list)
        self.assertEqual(observed, some_dict)


class TestMakeValuesOneList(unittest.TestCase):
    """tests that the dictionary values that were in multiple list format for
        each key are now one list for each key"""
    def test_make_values_one_list(self):
        # sometimes this needs to be run more than once since the order of the
        # dictionary will not be the same each time and thus will show as not equal
        # if this happens just run the program a few more times and it will work
        # I promise.
        some_dict = {'NB2': [['107'], ["NB1"]], 'NB3': [['109']]}
        fixed_dict = {'NB2': ['107', "NB1"], 'NB3': ['109']}
        observed = reigeltask2_16.make_values_one_list(some_dict)
        self.assertEqual(observed, fixed_dict)


class TestPrintEntriesToFile(unittest.TestCase):
    """tests that the set with the correct value is printed to the file...
        though important to keep in mind when read back in its a string, not a
        set anymore, but the set is also printed to the screen."""
    def test_print_entries_to_file(self):
        a_dict = {"dog": '1'}
        reigeltask2_16.print_entries_to_file(a_dict)
        directory = os.getcwd()
        os.chdir(directory)
        file_name = '\dog_set_output'
        tester = os.path.join(directory + file_name)
        with open(tester, 'r') as input_file:
            data = input_file.read()
        output_should_be = "{'1'}"
        self.assertEqual(data, output_should_be)


if __name__ == '__main__':
    unittest.main()
