from nbresult import ChallengeResultTestCase


class TestUnivariate(ChallengeResultTestCase):
    def test_squared_errors(self):
        self.assertEqual(self.result.squared_errors, [0, 0])

    def test_mse(self):
        self.assertEqual(self.result.mse, 0)

    def test_best_slope(self):
        self.assertGreater(self.result.theta1, 0.2)
        self.assertGreater(0.3, self.result.theta1)

    def test_best_intercept(self):
        self.assertGreater(self.result.theta0, 20)
        self.assertGreater(30, self.result.theta0)
