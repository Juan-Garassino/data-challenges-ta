from nbresult import ChallengeResultTestCase

class TestMergedDataframes(ChallengeResultTestCase):
    def test_merged_df_has_the_right_shape(self):
        self.assertEqual(self.result.merged_df_shape, (11, 2))

    def test_yearly_oil_value_2008(self):
        self.assertEqual(self.result.yearly_oil_2008, 34211)
