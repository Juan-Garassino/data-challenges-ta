from nbresult import ChallengeResultTestCase
import os

class TestGetData(ChallengeResultTestCase):
  def test_len(self):
    self.assertEqual(self.result.keys_len, 9)

  def test_columns(self):
    self.assertEqual(self.result.columns, ['seller_city', 'seller_id', 'seller_state', 'seller_zip_code_prefix'])

  def test_csv_exists(self):
    from os import walk
    wanted = ['olist_sellers_dataset.csv',
              'olist_order_reviews_dataset.csv',
              'olist_order_items_dataset.csv',
              'olist_customers_dataset.csv',
              'olist_orders_dataset.csv',
              'olist_order_payments_dataset.csv',
              'product_category_name_translation.csv',
              'olist_products_dataset.csv',
              'olist_geolocation_dataset.csv'
            ]
    csv_path = os.path.abspath(os.getcwd()).split('01-Project-Setup')[0] + "data" + os.sep + 'csv'
    _, _, actual = next(walk(csv_path))
    self.assertTrue(not bool(set(wanted) ^ set(actual) & set(wanted)), "Your missing some CSVs") # test if actual is a subset of wanted
