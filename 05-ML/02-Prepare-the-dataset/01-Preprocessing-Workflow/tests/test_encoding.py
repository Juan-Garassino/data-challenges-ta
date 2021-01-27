from nbresult import ChallengeResultTestCase


class TestEncoding(ChallengeResultTestCase):
    def test_garage_finish(self):
        self.assertEqual(len(self.result.dataset.columns), 12)

    def test_central_air(self):
        self.assertEqual(self.result.dataset.CentralAir.max(), 1)

    def test_month_sold(self):
        self.assertEqual(self.result.dataset.MoSold.max(), 1)
