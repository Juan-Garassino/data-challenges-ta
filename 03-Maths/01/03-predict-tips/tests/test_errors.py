import unittest
from compute_error import squared_errors, mean_squared_error

class TestError(unittest.TestCase):
    # Test for squared_errors
    def test_squared_errors_0(self):
        expected = [0, 0, 0]
        slope = 1
        intercept = 0
        total_bills = [0, 1, 2]
        tips = [0, 1, 2]
        self.assertEqual(squared_errors(slope, intercept, total_bills, tips), expected)

    def test_squared_errors_1(self):
        expected = [0, 0, 1]
        slope = 1
        intercept = 0
        total_bills = [0, 1, 2]
        tips = [0, 1, 1]
        self.assertEqual(squared_errors(slope, intercept, total_bills, tips), expected)

    def test_squared_errors_2(self):
        expected = [0, 1, 4]
        slope = 1
        intercept = 0
        total_bills = [0, 1, 2]
        tips = [0, 2, 4]
        self.assertEqual(squared_errors(slope, intercept, total_bills, tips), expected)

    def test_squared_errors_3(self):
        expected = [4, 16, 36]
        slope = 2
        intercept = 2
        total_bills = [0, 1, 2]
        tips = [0, 0, 0]
        self.assertEqual(squared_errors(slope, intercept, total_bills, tips), expected)

    def test_squared_errors_4(self):
        expected = [7.62, 21.90, 21.16]
        slope = 0.92
        intercept = 3
        total_bills = [3, 4, 5]
        tips = [3, 2, 3]
        errors = squared_errors(slope, intercept, total_bills, tips)
        for i in range(len(expected)):
            self.assertAlmostEqual(errors[i], expected[i], places = 2)


    # Test for mean_squared_error
    def test_mean_squared_errors_0(self):
        expected = 0
        slope = 1
        intercept = 0
        total_bills = [0, 1, 2]
        tips = [0, 1, 2]
        errors = squared_errors(slope, intercept, total_bills, tips)
        self.assertAlmostEqual(mean_squared_error(errors), expected, places = 2)

    def test_mean_squared_errors_1(self):
        expected = 1/3
        slope = 1
        intercept = 0
        total_bills = [0, 1, 2]
        tips = [0, 1, 1]
        errors = squared_errors(slope, intercept, total_bills, tips)
        self.assertAlmostEqual(mean_squared_error(errors), expected, places = 2)

    def test_mean_squared_errors_2(self):
        expected = 5/3
        slope = 1
        intercept = 0
        total_bills = [0, 1, 2]
        tips = [0, 2, 4]
        errors = squared_errors(slope, intercept, total_bills, tips)
        self.assertAlmostEqual(mean_squared_error(errors), expected, places = 2)

    def test_mean_squared_errors_3(self):
        expected = 56/3
        slope = 2
        intercept = 2
        total_bills = [0, 1, 2]
        tips = [0, 0, 0]
        errors = squared_errors(slope, intercept, total_bills, tips)
        self.assertAlmostEqual(mean_squared_error(errors), expected, places = 2)

    def test_mean_squared_errors_4(self):
        expected = sum([7.62, 21.90, 21.16])/3
        slope = 0.92
        intercept = 3
        total_bills = [3, 4, 5]
        tips = [3, 2, 3]
        errors = squared_errors(slope, intercept, total_bills, tips)
        self.assertAlmostEqual(mean_squared_error(errors), expected, places = 2)
