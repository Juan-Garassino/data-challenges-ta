import unittest
from pythagore import hypotenuse

class TestDebugMatrix(unittest.TestCase):
    def test_result(self):
        expected = 5
        self.assertEqual(hypotenuse(4, 3), expected)

    def test_negative_value(self):
        expected = 0
        self.assertEqual(hypotenuse(-5, 3), expected)

    def test_string_value(self):
        expected = 0
        self.assertEqual(hypotenuse("four", 3), expected)

    def test_zero_value(self):
        expected = 3
        self.assertEqual(hypotenuse(0, 3), expected)
