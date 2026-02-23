from day28_22_02_26 import rearrange_name
import unittest

# test case class
# create class which inhereits from test case

class testRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Ligma, Balls"
        expected = "Balls Ligma"
        self.assertEqual(rearrange_name(testcase),expected)
    # asta e un edge case --> e tot string dar nu e ceva ce neaparat ai testa de fiecare data 
    # trb sa fie handled manual usually
    def test_empty(self):
        testcase= ""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected)
    def test_dot(self):
        testcase="Saw, Kon D.Z."
        expected="Kon D.Z. Saw"
        self.assertEqual(rearrange_name(testcase),expected)
    # functiile TREBUIE sa inceapa cu test_ daca vrei sa fie rulate automat de unittest.main()
    def test_one_name(self):
        testcase='aaaa'
        expected='aaaa'
        self.assertEqual(rearrange_name(testcase),expected)

unittest.main()