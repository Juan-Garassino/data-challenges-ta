import unittest
from addition import addition_2_matrices

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 5, 7], [1, 15, 12], [7, 6, 4]]
C = [[2, 5, 7], [1, 15, 12], [7, 6, 4], [7, 6, 4]]

class TestDebugMatrix(unittest.TestCase):
    def test_result(self):
        expected = [[3, 7, 10],[5, 20, 18],[14, 14, 13]]
        self.assertEqual(addition_2_matrices(A,B), expected)

    def test_size_error(self):
        with self.assertRaises(IndexError):
            addition_2_matrices(A,C)
