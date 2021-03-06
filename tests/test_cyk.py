from unittest import TestCase
from cyk import cyk
from math import log


class TestCyk(TestCase):
    def setUp(self):
        self.rules = {("NP", "Det", "N"): 0.3,
                      ("Det", "The"): 0.4,
                      ("N", "flight"): 0.4}

        self.reverse_rules = {"The": ["Det"],
                              "flight": ["N"],
                              ("Det", "N"): ["NP"]}

    def test_with_two_words(self):
        result = cyk(self.rules, self.reverse_rules, "The flight")
        self.assertEquals(result, ("(NP (Det The)(N flight))", log(0.3*0.4*0.4)))