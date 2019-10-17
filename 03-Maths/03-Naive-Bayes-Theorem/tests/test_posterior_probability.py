import unittest
from posterior_probability import posterior_probability

class TestPosteriorProbability(unittest.TestCase):
    def test_sunny_if_yes(self):
        expected = 3/9
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(posterior_probability("Sunny", "Yes", weather, play), expected, places=2)

    def test_sunny_if_no(self):
        expected = 2/5
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(posterior_probability("Sunny", "No", weather, play), expected, places=2)

    def test_overcast_if_yes(self):
        expected = 4/9
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(posterior_probability("Overcast", "Yes", weather, play), expected, places=2)

    def test_rainy_if_no(self):
        expected = 3/5
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(posterior_probability("Rainy", "No", weather, play), expected, places=2)
