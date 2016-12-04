from unittest import TestCase
import training


class TestTraining(TestCase):
    def assert_exctract_symbol(self, rule, expected):
        self.assertEqual(training.extract_symbol(rule), expected)

    def test_extract_symbol(self):
        self.assert_exctract_symbol("(A (B b)(C c))", "A")
        self.assert_exctract_symbol("(ABC (BDH (DFDDF x)(FDSF f))(FDFSQ idsdf)", "ABC")
        self.assert_exctract_symbol("(DFFD fhdkfd)", "DFFD")

    # def assert_extract_rule(self, line, expected):
    #     self.assertEqual(training.parser(line), expected)
    #
    # def test_extract_rule(self):
    #     self.assert_extract_rule("(A test)", ["A", "test"])
    #     self.assert_extract_rule("(AB (GH test)(GFH hgy))", ["AB", "(GH test)", "(GFH hgy))"])


    def assert_splitcorrectly(self, line, expected):
        self.assertEqual(training.splitcorrectly(line), expected)

    def test_splitcorrectly(self):
        self.assert_splitcorrectly('(SALUT (WESH (WESHYO non)))(YO y)',('(SALUT (WESH (WESHYO non)))', '(YO y)'))
        self.assert_splitcorrectly('(SALUT (WESH (WESHYO non)))(YO y)', ('(SALUT (WESH (WESHYO non)))', '(YO y)'))

    def assert_test_sum_of_counts(self, dico, expected):
        self.assertEqual(training.sum_of_counts(dico), expected)

    def test_sum_of_counts(self):
        self.assert_test_sum_of_counts(training.newdico, {'A' : 3, 'R' : 2})

    # def assert_test_count_terminals(self, dico, expected):
    #     self.assertEqual(training.count_terminals(dico), expected)
    #
    # def test_count_terminals(self):
    #     self.assert_test_count_terminals(training.newdico2, 2)