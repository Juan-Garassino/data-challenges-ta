
from nbresult import ChallengeResultTestCase


class TestRidge(ChallengeResultTestCase):
    def test_top2(self):
        self.assertCountEqual(self.result.top_2_features, ['age', 'smoker'])
