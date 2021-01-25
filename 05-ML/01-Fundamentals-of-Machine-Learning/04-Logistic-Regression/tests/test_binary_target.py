from nbresult import ChallengeResultTestCase


class TestBinaryTarget(ChallengeResultTestCase):
    def test_binary_target_sum(self):
        self.assertEqual(sum(self.result.target), 881)
