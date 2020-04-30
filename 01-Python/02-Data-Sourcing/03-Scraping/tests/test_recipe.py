import unittest
from recipe import parse


class TestRecipe(unittest.TestCase):
    def test_parse_cucumber(self):
        recipes = parse(open('pages/tofu.html'))
        self.assertIsInstance(recipes, list, "The `parse` method should return a `list`")
        self.assertEqual(len(recipes), 15)
        self.assertIsInstance(recipes[0], dict, "The `parse` method should return a `list` of `dict` objects")
        self.assertEqual(recipes[0]['name'], 'Mapo tofu')
        self.assertEqual(recipes[0]['difficulty'], 'Easy')
        self.assertEqual(recipes[0]['prep_time'], '30 mins')
