from nbresult import ChallengeResultTestCase
import numpy as np


class TestGlobalOptimization(ChallengeResultTestCase):
    def test_bounds_is_a_list(self):
        self.assertIsInstance(self.result.bounds, list)

    def test_bounds_elements_are_tuples(self):
        for bound in self.result.bounds:
            self.assertIsInstance(bound, tuple)

    def test_bounds_values(self):
        for bound in self.result.bounds:
            self.assertEqual(bound, (-150, 150))

    def test_minimum_shgo_shape(self):
        self.assertEqual(self.result.Xmin_shgo.shape, (2,))

    def test_minimum_dual_shape(self):
        self.assertEqual(self.result.Xmin_dual.shape, (2,))

    def test_minimum_shgo_values(self):
        Xmin = self.result.Xmin_shgo
        self.assertTrue(np.all(Xmin <= 150))
        self.assertTrue(np.all(Xmin >= -150))

    def test_minimum_dual_values(self):
        Xmin = self.result.Xmin_dual
        self.assertTrue(np.all(Xmin <= 150))
        self.assertTrue(np.all(Xmin >= -150))
