import unittest
from recipe import parse

class TestRecipe(unittest.TestCase):
    def test_parse_cucumber(self):
        recipes = parse(open('pages/cucumber.html'))
        self.assertIsInstance(recipes, list, "The `parse` method should return a `list`")
        self.assertEqual(len(recipes), 10)
        self.assertIsInstance(recipes[0], dict, "The `parse` method should return a `list` of `dict` objects")
        self.assertEqual(recipes[0]['name'], 'Cucumber soup')
        self.assertEqual(recipes[0]['prep_time'], '50 min')
        self.assertEqual(recipes[0]['cooking_time'], '15 min')
