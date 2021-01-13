from nbresult import ChallengeResultTestCase
import numpy as np


class TestMinimizeConstraints(ChallengeResultTestCase):
    def test_starting_point_shape(self):
        self.assertEqual(self.result.X0.shape, (4,))

    def test_bounds_shape(self):
        self.assertEqual(len(self.result.bounds), 4)

    def test_bounds_is_tuple(self):
        self.assertIsInstance(self.result.bounds, tuple)

    def test_bounds_elements_are_tuples(self):
        for bound in self.result.bounds:
            self.assertIsInstance(bound, tuple)

    def test_bounds_values(self):
        for bound in self.result.bounds:
            self.assertEqual(bound, (1, 5))

    def test_minimum_shape(self):
        self.assertEqual(self.result.Xmin.shape, (4,))

    def test_first_constraint(self):
        first_constraint = np.sum(self.result.Xmin ** 2)
        self.assertAlmostEqual(first_constraint, 40)

    def test_second_constraint(self):
        Xmin = self.result.Xmin
        second_constraint = Xmin[0] * Xmin[1] * Xmin[2] * Xmin[3]
        self.assertGreater(25, second_constraint)

    def test_third_constraint(self):
        Xmin = self.result.Xmin
        self.assertTrue(np.all(Xmin <= 5))
        self.assertTrue(np.all(Xmin >= 1))
