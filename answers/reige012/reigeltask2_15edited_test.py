#!/usr/bin/env python
# encoding: utf-8

"""
Program uses unittest module to test the different units (i.e. functions) from
a previously written code (reigeltask2_15edited.py).

Edited by Alicia Reigel. 24 March 2016.
Copyright Alicia Reigel. Louisiana State University. 24 March 2016. All
rights reserved.

"""


import unittest
import datetime
import reigeltask2_15edited


class TestFormatDates(unittest.TestCase):

    def test_format_input_dates(self):
        observed = reigeltask2_15edited.format_input_dates(2016, 3, 24)
        self.assertEqual(observed, datetime.date(2016, 3, 24))


class TestFigureOutWeekends(unittest.TestCase):

    def test_figure_out_weekends(self):
        d1 = datetime.date(2016, 3, 24)
        d2 = datetime.date(2016, 3, 28)
        observed = reigeltask2_15edited.figure_out_weekends(d1, d2)
        self.assertEqual(observed, 2)


if __name__ == '__main__':
    unittest.main()
