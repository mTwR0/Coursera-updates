from day28_22_02_26 import rearrange_name
import unittest

# test case class
# create class which inhereits from test case

class testRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Ligma, Balls"
        expected = "Balls Ligma"
        self.assertEqual(rearrange_name(testcase),expected)