import unittest
from euclidean_distance_nd import euclidean_distance_p2p
import random

class TestDistanceND(unittest.TestCase):
    def test_same_point(self):
        expected = 0
        p = [0]
        self.assertAlmostEqual(euclidean_distance_p2p(p, p), expected, places=2)

    def test_10d_pointst(self):
        expected = 15.87
        p_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        p_2 = [1, 0, 4, 7, 0, 1, 8, 3, 0,1]
        self.assertAlmostEqual(euclidean_distance_p2p(p_1, p_2), expected, places=2)

    def test_100d_pointst(self):
        expected = 799.38
        random.seed(1)
        p_1 = [random.uniform(-100, 100) for i in range(100)]
        p_2 = [random.uniform(-100, 100) for i in range(100)]
        self.assertAlmostEqual(euclidean_distance_p2p(p_1, p_2), expected, places=2)
