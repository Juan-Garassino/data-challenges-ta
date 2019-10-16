import unittest
from transpose import transpose

A = [   [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
B = [   [2, 5, 7],
        [1, 15, 12],
        [7, 6, 4]
    ]
C = [   [2, 5, 7],
        [1, 15, 12],
        [7, 6, 4],
        [7, 6, 4]
    ]

class TestTranspose(unittest.TestCase):
    def test_square_matrix(self):
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose(A), expected)

    def test_non_square_matrix(self):
        expected = [[2, 1, 7, 7], [5, 15, 6, 6], [7, 12, 4, 4]]
        self.assertEqual(transpose(C), expected)

    def test_transpose_row(self):
        expected = [[2], [1], [7], [7]]
        self.assertEqual(transpose([[2, 1, 7, 7]]), expected)

    def test_transpose_col(self):
        expected = [[2, 1, 7, 7]]
        self.assertEqual(transpose([[2], [1], [7], [7]]), expected)
