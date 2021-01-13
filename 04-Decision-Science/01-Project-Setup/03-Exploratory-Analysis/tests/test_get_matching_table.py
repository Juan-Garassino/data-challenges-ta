from olist.data import Olist
import unittest

class TestGetMatchingTable(unittest.TestCase):
  data = Olist().get_matching_table()

  def test_rows(self):
    self.assertEqual(self.__class__.data.shape[0], 114100)

  def test_columns_len(self):
    self.assertEqual(len(list(self.__class__.data.columns)), 5)

  def test_column_names(self):
    self.assertEqual(sorted(list(self.__class__.data.columns)), ['customer_id', 'order_id', 'product_id', 'review_id', 'seller_id'])
