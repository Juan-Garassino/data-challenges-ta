import unittest
from data_cleaning import missing_data, datetime_columns

class TestDataCleaning(unittest.TestCase):
   def test_missing_data_columns(self):
       expected = ['review_comment_message', 'review_comment_title',
                   'order_delivered_carrier_date', 'order_delivered_customer_date',
                   'product_category_name', 'product_description_lenght',
                   'product_name_lenght', 'product_photos_qty']
       test_list = missing_data()
       self.assertEqual(sorted(test_list), sorted(expected))

   def test_datetime_columns(self):
       expected = ['order_estimated_delivery_date',
                   'order_purchase_timestamp',
                   'shipping_limit_date', 'review_answer_timestamp',
                   'review_creation_date']
       test_list = datetime_columns()
       self.assertEqual(sorted(test_list), sorted(expected))
