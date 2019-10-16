import unittest
from basic_functions import matrix_ij, multiply_matrix, matrix_size, add_scalar2matrix, get_column

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 5, 7], [1, 15, 12], [7, 6, 4]]
C = [[2, 5, 7], [1, 15, 12], [7, 6, 4], [1, 2, 3]]

class TestDebugMatrix(unittest.TestCase):
    def test_M_12(self):
        expected = 6
        self.assertEqual(matrix_ij(A,1,2), expected)

    def test_M_00(self):
        expected = 1
        self.assertEqual(matrix_ij(A,0,0), expected)

    def test_M_ij_out_of_range(self):
        with self.assertRaises(IndexError):
            matrix_ij(A,7,2)



    def test_multiply_M(self):
        expected = [[4, 10, 14], [2, 30, 24], [14, 12, 8]]
        self.assertEqual(multiply_matrix(B, 2), expected)

    def test_double_zeros(self):
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(multiply_matrix(expected, 2), expected)



    def test_size_M(self):
        expected = (4,3)
        self.assertEqual(matrix_size(C), expected)

    def test_size_11(self):
        expected = (1,1)
        self.assertEqual(matrix_size([[1]]), expected)



    def test_add_one2M(self):
        expected = [[3, 6, 8], [2, 16, 13], [8, 7, 5], [2, 3, 4]]
        self.assertEqual(add_scalar2matrix(C, 1), expected)



    def test_get_column(self):
        expected = [1, 4, 7]
        self.assertEqual(get_column(A,0), expected)

    def test_get_column_out_of_range(self):
        with self.assertRaises(IndexError):
            get_column(A,7)

