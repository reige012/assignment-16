import unittest
import A9T1


class TestA9T1center(unittest.TestCase):

    def test_aestr1(self):
        observed = A9T1.aestr1('thirty')
        expected = '~~~~~~~~~~~~thirty~~~~~~~~~~~~'
        self.assertEqual(observed, expected)


class TestA9T1stripsplit(unittest.TestCase):

    def aestr2(self):
        observed = A9T1.aestr2('\nthis is a string\n')
        expected = 'this\
                    is\
                    a\
                    string'
        self.assertEqual(observed, expected)


class TestA9T1find(unittest.TestCase):

    def aestr3(self):
        observed = A9T1.aestr3('this is a string of something')
        #will return the position of the 'string' within the str.
        expected = 8
        self.assertEqual(observed, expected)


class TestA9T1count(unittest.TestCase):

    def aestr4(self):
        observed = A9T1.aestr4("aaa's")
        #returns the count of each 'a' in accending order.
        expected = '1\
                    2\
                    3'
        self.assertEqual(observed, expected)


class TestA9T1upper(unittest.TestCase):

    def AEstr5(self):
        observed = A9T1.AEstr5('speaking of this.')
        expected = 'SPEAKING OF THIS!'
        self.assertEqual(observed, expected)

if __name__ == '__main__':
    unittest.main()
