from nbresult import ChallengeResultTestCase
import numpy as np

class TestOlympicGames(ChallengeResultTestCase):
    def test_summer_countries_df_shape(self):
        self.assertEqual(self.result.summer_countries_shape, (25742, 13))

    def test_all_countries_df_shape(self):
        self.assertEqual(self.result.all_countries_shape, (30568, 13))

    def test_top_10_countries_medals(self):
        self.assertEqual(self.result.top_country_1, 2472)
        self.assertEqual(self.result.top_country_10, 563)
