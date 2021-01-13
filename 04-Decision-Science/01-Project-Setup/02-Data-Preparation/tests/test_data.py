import unittest

class TestGetData(unittest.TestCase):
  def test_olist_is_imported(self):
    result = False
    message = ''
    try:
      from olist.data import Olist
      result = True
    except:
      message = "Can't seem to import Olist module"
    self.assertTrue(result, message)

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
    _, _, actual = next(walk('../../data/csv'))
    self.assertTrue(not bool(set(wanted) ^ set(actual) & set(wanted)), "Your missing some CSVs") # test if actual is a subset of wanted

  def test_get_data(self):
    from olist.data import Olist
    data = Olist().get_data()
    self.assertTrue(data, "your get_data method doesn't seenm to work properly")
    self.assertEqual(len(data), 9)
    self.assertEqual(sorted(list(data['sellers'].columns)), ['seller_city', 'seller_id', 'seller_state', 'seller_zip_code_prefix'])

