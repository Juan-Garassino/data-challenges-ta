import os
import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist


class Order:

    def __init__(self):
        self.data = Olist().get_data()

    def get_wait_time(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, wait_time, expected_wait_time ,delay_vs_expected
        """

    def get_review_score(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """

    def get_number_products(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_products
        """

    def get_number_sellers(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, number_of_products
        """

    def get_price_and_freight(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, price, freight_value
        """

    def get_distance_seller_customer(self):
        """
        02-01 > Returns a DataFrame with order_id
        and distance between seller and customer
        """

    def get_training_data(self):
        """
        02-01 > Returns a DataFrame with:
        order_id, wait_time, wait_vs_expected,
        dim_is_five_star, dim_is_one_star, number_of_product,
        number_of_sellers, freight_value, distance_customer_seller
        """
