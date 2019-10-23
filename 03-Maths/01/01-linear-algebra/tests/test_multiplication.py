import unittest
from product import multiply_matrices

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

class TestDebugMatrix(unittest.TestCase):
    def test_result(self):
        expected = [[ 25,  53,  43],
       [ 55, 131, 112],
       [ 85, 209, 181]]
        self.assertEqual(multiply_matrices(A,B), expected)

    def test_size_error(self):
        with self.assertRaises(IndexError):
            multiply_matrices(A,C)
