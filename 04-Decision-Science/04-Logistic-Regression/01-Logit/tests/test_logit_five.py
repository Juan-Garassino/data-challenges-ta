from nbresult import ChallengeResultTestCase

class TestLogitFive(ChallengeResultTestCase):

  def test_intercept_five(self):
    self.assertAlmostEqual(self.result.intercept_five, 2.43)
