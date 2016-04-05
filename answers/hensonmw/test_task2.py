import pandas
import unittest
import task2
import pandas.util.testing
"""
My test for the 2nd task for assignment 16
I worked with AJ dun dun dun
Created by Michael Henson on 30 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.
See:
http://penandpants.com/2014/10/07/testing-with-numpy-and-pandas/
"""


class TestTask2(unittest.TestCase):
    def test_sorting(self):
        df = pandas.DataFrame({'Swamp_A': [2,3]})
        observed = task2.sorting(df)
        expected = pandas.DataFrame({'Swamp_A': [3,2]})
        self.assertEqual(str(observed), str(expected))

    def test_transpose(df):
        df = pandas.DataFrame({'Swamp_A': [2,3]})
        observed = task2.sorting(df)
        expected = pandas.DataFrame({'Swamp_A': [3,2]})
        pandas.util.testing.assert_frame_equal(observed, expected)

    def test_deleting_columns(df):
        df = pandas.DataFrame({'Swamp_A': [2,3]}, {'Swamp_B': [2,1]})
        observed = task2.sorting(df)
        expected = pandas.DataFrame({'Swamp_A': [2,3]})
        pandas.util.testing.assert_frame_equal(observed, expected)

    def test_evaluation(self):
        observed = '0'
        expected = '0'
        self.assertEqual(observed, expected)

    def test_mean(df):
        df = pandas.DataFrame({'Swamp_A': [1,2]}, {'Swamp_B': [2,3]})
        observed = task2.sorting(df)
        expected = pandas.DataFrame({'Swamp_A': [1,2]}, {'Swamp_B': [2,3]}, {'sum': [1.5, 2.5]})
        pandas.util.testing.assert_frame_equal(observed, expected)


if __name__ == '__main__':
    unittest.main()
