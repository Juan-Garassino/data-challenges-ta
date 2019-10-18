# pylint: disable-all

import unittest
import statistics
import numpy as np 
from basic_functions import *

class TestBasicFunctions(unittest.TestCase):
    def test_mean(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(mean(test1), statistics.mean(test1))
    
    def test_standard_deviation(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(standard_deviation(test1), statistics.stdev(test1))

    def test_median(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(median(test1), statistics.median(test1))
        test2 = [5,3,4,6,0,2,1]
        self.assertEqual(median(test2), statistics.median(test2))
        test3 = [5,3,4,6,0,2]
        self.assertEqual(median(test3), statistics.median(test3))

    def test_mode(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(mode(test1), statistics.mode(test1))
        test2 = ["a","a","b","c"]
        self.assertEqual(mode(test2), statistics.mode(test2))
        test3 = [5,3,4,6,0,2,2]
        self.assertEqual(mode(test3), statistics.mode(test3))

    def test_quartiles(self):
        test1 = [1,2,3,4,5]
        self.assertEqual(quartiles(test1), [1.5,3,4.5])
        test2 = [6,3,4,5,2,1]
        self.assertEqual(quartiles(test2), [2,3.5,5])
        self.assertEqual(quartiles([2,4,9]), [2,4,9])
        self.assertEqual(quartiles([2,9]), [2,5.5,9])
