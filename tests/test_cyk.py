from unittest import TestCase
from cyk import cyk

class TestCyk(TestCase):
    def setUp(self):
        self.rules = {("NP", "Det", "N"): 0.3,
                      ("Det", "The"): 0.4,
                      ("N", "flight"): 0.4}

        self.reverse_rules = {"The": ["Det"],
                              "flight": ["N"],
                              ("Det", "N"): ["NP"]}

    def test_with_one_word(self):
        result = cyk(self.rules, self.reverse_rules, "The")
        self.assertEquals(result, ("(Det The)", 0.4))