# !/usr/bin/env python
# encoding: utf-8


"""
My testing of cites_task2.py (assignment-16) program
Created by Andre Moncrieff on 22 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import unittest
import openpyxl
import argparse
import re
import csv
import os

from collections import Counter
from operator import itemgetter

import cites_task2


class TestCitesTask2(unittest.TestCase):
    def path(self):
        """
        To user/grader: paste in your path below for the task2_test_files
        """
        return "/Users/Andre/Desktop/Comp_Prog_for_Biologists/assignment-16/answers/AndreMonc/task2_files/task2_test_files"

    def path2(self):
        """
        To user/grader: paste in your path below for the task2_files
        """
        return "/Users/Andre/Desktop/Comp_Prog_for_Biologists/assignment-16/answers/AndreMonc/task2_files"

    def expected_list(self):
        return ['Accipiter bicolor', 'Accipiter collaris',
                'Accipiter poliogaster', 'Accipiter striatus',
                'Accipiter superciliosus', 'Busarellus nigricollis',
                'Buteo albigula', 'Buteo albonotatus', 'Buteo brachyurus',
                'Correct birdname', 'Correct species']

    def test_cites_list_cleaner(self):
        os.chdir(self.path())
        observed = cites_task2.cites_list_cleaner('Test_Raw_Cites.xlsx', 2)
        expected = self.expected_list()
        self.assertEqual(observed, expected)
        return observed

    def test_write_cleaned_cites_to_excel(self):
        cites_task2.write_cleaned_cites_to_excel(self.expected_list())
        cleaned_cites_list = cites_task2.cites_list_cleaner(
                             "clean_cites_list_of_Peruvian_birds.xlsx", 1)
        observed = cleaned_cites_list
        expected = self.expected_list()
        self.assertEqual(observed, expected)

    def test_make_trip_list(self):
        os.chdir(self.path())
        test_list = "Test_Trip_List.xlsx"
        observed = cites_task2.make_trip_list(test_list)
        expected = ['Contopus sordidulus', 'Anabazenops dorsalis',
                    'Turdus leucops', 'Colonia colonus',
                    'Anabazenops dorsalis', 'Ramphocelus carbo',
                    'Microcerculus marginatus', 'Poecilotriccus latirostris',
                    'Synallaxis cabanisi', 'Dysithamnus mentalis',
                    'Correct species']
        self.assertEqual(observed, expected)
        return observed

    def test_trip_list_counted(self):
        hypothetical_trip_list = self.test_make_trip_list()
        raw_obs_list = []
        raw_exp_list = []
        observed_dict = cites_task2.trip_list_counted(hypothetical_trip_list)
        expected_dict = dict(Counter(hypothetical_trip_list))
        for key, value in observed_dict.items():
            raw_obs_list.append([key, value[0]])
        for key, value in expected_dict.items():
            raw_exp_list.append([key, value])
        observed = sorted(raw_obs_list, key=itemgetter(0))[::-1]
        expected = sorted(raw_exp_list, key=itemgetter(0))[::-1]
        self.assertEqual(observed, expected)

    def test_add_cites_status_to_dict(self):
        os.chdir(self.path())
        hypothetical_trip_list = self.test_make_trip_list()
        expected_status_dict = {"Accipiter striatus": "Cites",
                                "Contopus sordidulus": "No Cites"}
        trip_num_dict = cites_task2.trip_list_counted(hypothetical_trip_list)
        cites_list = self.test_cites_list_cleaner()
        computed_status_dict = cites_task2.add_cites_status_to_dict(
                               trip_num_dict, cites_list)
        observed = computed_status_dict["Contopus sordidulus"][1]
        expected = expected_status_dict["Contopus sordidulus"]
        self.assertEqual(observed, expected)

    def test_write_summary_to_csv(self):
        os.chdir(self.path2())
        with open("cites_summary.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            line_number = 2
            reader = list(reader)
            test_text = reader[line_number]
            observed = (type(test_text[0]),
                        type(int(test_text[1])),
                        type(test_text[0]))
            expected = (type("bird name"), type(1), type("cites status"))
            self.assertEqual(observed, expected)

if __name__ == '__main__':
    unittest.main()
