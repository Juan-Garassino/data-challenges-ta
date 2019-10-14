# pylint: disable-all

import unittest
import os.path

class TestExerciseDone(unittest.TestCase):
    def test_exercise_done(self):
        f = os.path.isfile("Exercise_04.ipynb") 
        self.assertEqual(f, True)
