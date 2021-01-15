from nbresult import ChallengeResultTestCase

class TestLogitOne(ChallengeResultTestCase):

  def test_intercept_one(self):
    self.assertAlmostEqual(self.result.intercept_one, -5.15)
