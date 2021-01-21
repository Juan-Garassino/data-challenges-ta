from nbresult import ChallengeResultTestCase


class TestKnn(ChallengeResultTestCase):
    def test_best_k(self):
        self.assertEqual(self.result.best_k, 16)

    def test_best_score(self):
        self.assertGreater(self.result.best_score, 0.76)
