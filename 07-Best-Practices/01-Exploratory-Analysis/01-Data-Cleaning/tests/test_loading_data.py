import unittest
from olist.data import Olist


class TestLoadData(unittest.TestCase):
    def test_keys_load_data(self):
        data = Olist().get_data()
        keys = list(data.keys())
        expected = ['olist_sellers_dataset', 'product_category_name_translation',
                    'olist_orders_dataset', 'olist_order_items_dataset',
                    'olist_customers_dataset', 'olist_geolocation_dataset',
                    'olist_order_payments_dataset', 'olist_order_reviews_dataset',
                    'olist_products_dataset']
        self.assertEqual(sorted(keys), sorted(expected))

    def test_order_shape(self):
        data = Olist().get_data()
        shape_order = data['olist_orders_dataset'].shape
        self.assertEqual(shape_order, (99441, 8))