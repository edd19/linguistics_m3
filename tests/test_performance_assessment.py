from unittest import TestCase
from performance_assessment import assess_perfomance


class TestPerformanceAssessment(TestCase):
    def test_single_sentence(self):
        gold_standard = "(SBARQ (WHNP what)(SBARQ (SQ (VBZ does)(SQ (NP (DT the)(NP (NNP peugeot)(<NN> company)))" \
                        "(VP manufacture)))(<.> ?)))"
        actual = "(SBARQ (WHNP what)(SBARQ (SQ (VBZ does)(NP (DT the)(NP (NNP peugeot)(NP (<NN> company)" \
                 "(<NN> manufacture)))))(<?> ?)))"
        result = assess_perfomance(gold_standard, actual)
        self.assertEquals(result, (8, 13, 13))
