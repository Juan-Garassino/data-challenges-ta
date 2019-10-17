import unittest
import random
import matplotlib.pyplot as plt
from euclidean_distance_2d import euclidean_distance_p2p, euclidean_distance_p2dr, points_in_circle, hypotenuse_with_points, error_predictions

class TestEuclideanDistance2D(unittest.TestCase):
    # Test for euclidean_distance_p2p
    def test_same_point(self):
        expected = 0
        self.assertEqual(euclidean_distance_p2p([3, 4], [3, 4]), expected)

    def test_origine(self):
        expected = 0
        self.assertEqual(euclidean_distance_p2p([0, 0], [0, 0]), expected)

    def test_negative_value(self):
        expected = 65**0.5
        self.assertAlmostEqual(euclidean_distance_p2p([-10, 3], [-2, 4]), expected, places=2)

    def test_x_axis(self):
        expected = 22
        self.assertEqual(euclidean_distance_p2p([-10, 0], [12, 0]), expected)

    # Test for hypotenuse_with_points
    def test_hypotenuse_same_point(self):
        expected = 0
        self.assertEqual(hypotenuse_with_points([0, 0], [0, 0], [0, 0]), expected)

    def test_hypotenuse_same_line(self):
        expected = 1
        self.assertEqual(hypotenuse_with_points([0, 1], [0, 2], [0, 2]), expected)

    def test_hypotenuse_result(self):
        expected = 12.25
        self.assertAlmostEqual(hypotenuse_with_points([0, 0], [0, 5], [10, 0]), expected, places=2)

    # Test for euclidean_distance_p2dr
    def test_p2d_test1(self):
        expected = 1.41
        self.assertAlmostEqual(euclidean_distance_p2dr([-1, 1], 1, 0), expected, places=2)

    def test_p2d_zero(self):
        expected = 0
        self.assertEqual(euclidean_distance_p2dr([0, 3], 6, 3), expected)

    def test_p2d_test2(self):
        expected = 7.52
        self.assertAlmostEqual(euclidean_distance_p2dr([7, 2], 4, 5), expected, places=2)

    # Test for error_predictions
    def test_no_error(self):
        expected = [0, 0, 0, 0, 0]
        y = [(1, 2),(3, 4),(5, 6),(7, 8),(9, 10)]
        self.assertEqual(error_predictions(y,y), expected)

    def test_error_result(self):
        expected = [1.0, 2.0, 1.0, 0.0, 3.0]
        y = [(1, 2),(3, 4),(5, 6),(7, 8),(9, 10)]
        predictions = [(1, 3),(1, 4),(5, 7),(7, 8),(12, 10)]
        self.assertEqual(error_predictions(y,predictions), expected)

    # Test for points_in_circle
    def test_points_in_circle(self):
        random.seed(1)
        R = 4
        X = []
        C = (0,0)
        for i in range(100):
            x = round(random.uniform(-R, R), 2)
            y = round(random.uniform(-R, R), 2)
            X.append([x,y])
        results = points_in_circle(X, C, R)
        expected=[[2.11, -1.96], [-0.04, -0.4], [1.21, 2.31], [2.69, -0.54], [-0.44, 1.77], [-3.8, 0.33], [3.51, -0.95], [-2.27, -0.62], [-0.5, -0.03], [-2.14, -2.15], [-2.25, -0.32], [2.7, 0.45], [1.14, -2.51], [-3.03, -1.34], [1.77, 1.69], [3.49, -0.62], [2.64, 1.36], [-1.57, 0.7], [0.04, 0.71], [2.38, -0.69], [-2.62, 0.39], [1.62, 1.4], [-1.0, -0.49], [0.07, 2.23], [0.17, -0.85], [-0.08, -3.76], [-3.65, 1.63], [3.87, 0.75], [-0.85, -2.64], [0.02, 3.86], [2.16, 0.32], [2.88, -2.14], [0.11, 3.62], [0.62, -0.33], [-1.85, 0.38], [2.27, 2.56], [3.09, 1.92], [2.47, 0.15], [0.49, -0.59], [0.56, -2.4], [0.04, -0.12], [-1.15, -1.23], [0.31, 0.99], [0.9, -0.33], [-2.58, 0.68], [2.89, 2.39], [2.38, 2.53], [-1.96, 2.73], [1.38, -3.33], [2.04, -2.0], [-3.12, 1.0], [-1.24, -3.44], [-2.72, 0.22], [-2.65, -1.82], [1.69, -0.36], [-1.42, -0.21], [-3.81, -0.91], [-0.63, -2.5], [0.08, -2.33], [0.85, 2.54], [-2.83, 1.75], [-2.72, 1.64], [1.43, 0.36], [2.38, 0.13], [-2.21, 1.19], [-0.84, 0.61], [-1.43, 1.05], [-3.53, -1.61], [-1.55, 2.87], [-1.52, 3.51], [1.95, -0.67], [0.56, -2.63], [1.63, 0.07], [-0.98, -1.22], [-2.35, 1.39], [-0.54, -2.45], [-3.16, 1.33], [-1.63, -0.0]]
        # circle1 = plt.Circle(C, R, color='r', fill=False)
        # plt.gcf().gca().add_artist(circle1)
        # for p in results:
        #     plt.plot(p[0], p[1], 'gX')
        # plt.show()
        self.assertEqual(results, expected)
