from unittest import TestCase
import training


class TestTraining(TestCase):
    def assert_exctract_symbol(self, rule, expected):
        self.assertEqual(training.extract_symbol(rule), expected)

    def test_extract_symbol(self):
        self.assert_exctract_symbol("(A (B b)(C c))", "A")
        self.assert_exctract_symbol("(ABC (BDH (DFDDF x)(FDSF f))(FDFSQ idsdf)", "ABC")
        self.assert_exctract_symbol("(DFFD fhdkfd)", "DFFD")

    def assert_extract_rule(self, line, expected):
        self.assertEqual(training.parser(line), expected)

    def test_extract_rule(self):
        self.assert_extract_rule("(A test)", ["A", "test"])
        self.assert_extract_rule("(AB (GH test)(GFH hgy))", ["AB", "(GH test)", "(GFH hgy))"])

