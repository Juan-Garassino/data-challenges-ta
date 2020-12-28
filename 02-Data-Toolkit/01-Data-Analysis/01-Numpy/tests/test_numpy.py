from nbresult import ChallengeResultTestCase
import numpy as np

class TestNumpy(ChallengeResultTestCase):
    def test_vectors_creation(self):
        assert np.array_equal(self.result.ten, np.zeros(10))
        assert np.array_equal(self.result.from_five, np.arange(5, 11))

    def test_ndarrays_creation(self):
        assert np.array_equal(self.result.A, np.array([[5, 9, 7], [1, 0, 3]]))
        assert np.array_equal(self.result.B, np.ones((2,2), dtype=int))

    def test_linear_twenty_vector_creation(self):
        assert np.array_equal(self.result.lin_twenty, np.linspace(-1, 1, 20))

    def test_matrixes_creation_and_reshaping(self):
        assert np.array_equal(self.result.C, np.eye(3, dtype='int'))
        D = np.array([2, 9, 7, 3, 1, 5])
        assert np.array_equal(self.result.E, D.reshape(2, 3))
        checkboard = np.tile(np.array([[1,0],[0,1]]), (4, 4))
        assert np.array_equal(self.result.F, checkboard)

    def test_advanced_matrixes_manipulation(self):
        self.assertEqual(self.result.reshaped_G.shape, (4, 1))
        G = np.array([0, 4, -4, -3, 1, 1]).reshape(3, 2)
        H = np.array([[0, 1], [1, -1], [2, 3]])
        assert np.array_equal(self.result.gh_sum, G + H)
