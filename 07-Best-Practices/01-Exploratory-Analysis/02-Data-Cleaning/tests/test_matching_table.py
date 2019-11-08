import unittest
from ...olist.data import Olist


class TestMatchingTable(unittest.TestCase):
    def test_keys_matching_table(self):
        matching_table = Olist().get_matching_table()
        keys = list(matching_table.keys())
        expected = ['customer_id', 'customer_unique_id', 'order_id',
                    'product_id', 'seller_id']
        self.assertEqual(sorted(keys), sorted(expected))

    def test_matching_table_shape(self):
        matching_table = Olist().get_matching_table()
        shape_matching = matching_table.shape
        self.assertEqual(shape_matching, (110197, 5))
