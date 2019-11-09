import unittest
from CompareStrings import CompareStrings


class TestCompareStrings(unittest.TestCase):
    def test_calculation():
        #Test that we are finding relation properly
        self.asserAlmostEqual(CompareStrings("Address is missing", "NM109 is not correct"), "33%")


CompareStrings("testing this string", "This string is testing stuff") # => 100%
CompareStrings("Address is missing", "NM109 is not correct") # => 33%
