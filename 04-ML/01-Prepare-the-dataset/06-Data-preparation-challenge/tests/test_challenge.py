# pylint: disable-all

import unittest
from utils import model

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        expected = 0.8
        actual = model()
        self.assertGreater(actual,expected , 2)
