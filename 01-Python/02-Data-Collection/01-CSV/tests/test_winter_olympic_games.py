# pylint: disable-all

import unittest

from winter_olympic_games import most_decorated_athlete_ever
from winter_olympic_games import country_with_most_gold_medals

class TestWinterOlympicGames(unittest.TestCase):
    def test_most_decorated_athlete_ever(self):
        athlete = most_decorated_athlete_ever()
        self.assertEqual(athlete, 'BJOERNDALEN, Ole Einar')

    def test_country_with_most_gold_medals_between_2002_and_2014(self):
        country = country_with_most_gold_medals(2002, 2014)
        self.assertEqual(country, 'Canada')

    def test_country_with_most_gold_medals_between_1924_and_1972(self):
        country = country_with_most_gold_medals(1994, 1998)
        self.assertEqual(country, 'Germany')
