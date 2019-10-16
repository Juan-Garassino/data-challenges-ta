import unittest
from compute_error import get_errors

class TestError(unittest.TestCase):
    def test_get_erros(self):
        expected = 5
        self.assertEqual(get_errors(), expected)

