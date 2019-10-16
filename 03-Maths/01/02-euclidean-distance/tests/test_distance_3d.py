import unittest
from euclidean_distance_3d import distance_3d, points_in_sphere
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

class TestDistance3D(unittest.TestCase):
    # Tests for distance function
    def test_same_point(self):
        p = [0,0,0]
        expected = 0
        self.assertAlmostEqual(distance_3d(p, p), expected, places = 2)

    def test_result_1(self):
        p_1 = [0, 0, 0]
        p_2 = [1, 0, 0]
        expected = 1
        self.assertEqual(distance_3d(p_1, p_2), expected)

    def test_result_1(self):
        p_1 = [7, 21, 104]
        p_2 = [23, -8, 14]
        expected = 95.90
        self.assertAlmostEqual(distance_3d(p_1, p_2), expected, places = 2)

    # Tests for points_in_sphere function
    def test_points_in_sphere(self):
        random.seed(1)
        R = 4
        X = []
        C = (0, 0, 0)
        for i in range(100):
            x = round(random.uniform(-R, R), 2)
            y = round(random.uniform(-R, R), 2)
            z = round(random.uniform(-R, R), 2)
            X.append([x, y, z])
        results = points_in_sphere(X, C, R)
        expected = [[-1.96, -0.04, -0.4], [0.33, 3.51, -0.95], [-2.23, -0.5, -0.03], [-2.14, -2.15, -2.25]]

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_aspect("equal")
        print(results)
        for r in results:
            ax.scatter([r[0]], [r[1]], [r[2]], color="g", s=10)
        # draw sphere
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = R * (np.cos(u)*np.sin(v)) + C[0]
        y = R * (np.sin(u)*np.sin(v)) + C[1]
        z = R * (np.cos(v)) + C[2]
        ax.plot_wireframe(x, y, z, color="r")
        plt.show()
        self.assertAlmostEqual(results[0:4], expected, places=2)
