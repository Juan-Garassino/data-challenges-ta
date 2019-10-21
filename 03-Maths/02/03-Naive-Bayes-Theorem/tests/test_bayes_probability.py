import unittest
from bayes_probability import bayes_probability

class TestBayesProbability(unittest.TestCase):
    def test_yes_if_sunny(self):
        expected = 0.6
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(bayes_probability("Yes", "Sunny", play, weather), expected, places=2)

    def test_yes_if_rainy(self):
        expected = 0.4
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(bayes_probability("Yes", "Rainy", play, weather), expected, places=2)

    def test_yes_if_overcast(self):
        expected = 1
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(bayes_probability("Yes", "Overcast", play, weather), expected, places=2)

    def test_no_if_sunny(self):
        expected = 0.4
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(bayes_probability("No", "Sunny", play, weather), expected, places=2)

    def test_no_if_rainy(self):
        expected = 0.6
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(bayes_probability("No", "Rainy", play, weather), expected, places=2)

    def test_no_if_overcast(self):
        expected = 0
        weather = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
        'Rainy','Sunny','Overcast','Overcast','Rainy']
        play = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
        self.assertAlmostEqual(bayes_probability("No", "Overcast", play, weather), expected, places=2)

    def test_bayes_100_data_no_if_overcast(self):
        expected = 0.56
        weather = ['Overcast', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Overcast', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Rainy', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Sunny', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Sunny', 'Rainy', 'Overcast', 'Sunny', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Sunny', 'Sunny', 'Sunny']
        play =['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
        self.assertAlmostEqual(bayes_probability("No", "Overcast", play, weather), expected, places=2)

    def test_bayes_100_data_yes_if_sunny(self):
        expected = 0.65
        weather = ['Sunny', 'Overcast', 'Sunny', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Sunny', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Rainy', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Sunny', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Sunny', 'Rainy', 'Overcast', 'Sunny', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Sunny', 'Sunny', 'Sunny']
        play =['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
        self.assertAlmostEqual(bayes_probability("Yes", "Sunny", play, weather), expected, places=2)

    def test_bayes_100_data_no_if_rainy(self):
        expected = 0.62
        weather = ['Rainy', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Overcast', 'Sunny', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Rainy', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Overcast', 'Sunny', 'Sunny', 'Overcast', 'Sunny', 'Overcast', 'Overcast', 'Overcast', 'Sunny', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Sunny', 'Rainy', 'Overcast', 'Sunny', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Sunny', 'Sunny', 'Sunny']
        play =['No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
        self.assertAlmostEqual(bayes_probability("Yes", "Sunny", play, weather), expected, places=2)




