import unittest
from prior_probability import prior_probability

class TestPriorProbability(unittest.TestCase):
    def test_weather_sunny(self):
        expected = 0.5
        weather = ['Sunny','Overcast','Rainy','Sunny']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(prior_probability("Sunny",weather), expected, places=2)

    def test_weather_overcast(self):
        expected = 0.25
        weather = ['Sunny','Overcast','Rainy','Sunny']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(prior_probability("Overcast",weather), expected, places=2)

    def test_play_yes(self):
        expected = 0.8
        play = ['No','Yes','Yes','Yes','Yes']
        self.assertAlmostEqual(prior_probability("Yes",play), expected, places=2)

    def test_play_no(self):
        expected = 0.2
        play = ['No','Yes','Yes','Yes','Yes']
        self.assertAlmostEqual(prior_probability("No",play), expected, places=2)
