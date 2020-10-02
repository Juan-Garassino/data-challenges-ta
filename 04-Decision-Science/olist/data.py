import os
import pandas as pd


class Olist:

    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrame loaded from csv files
        """
        # Hint: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Hint2: Use __file__ as absolute path anchor to avoid displaying your username or computer-specific folder architecture.
        # Hint3: Use os.path library to construct path independent of Unix vs. Windows specificities

    def get_matching_table(self):
        """
        01-01 > This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """

    def ping(self):
        """
        You call ping I print pong.
        """
        print('pong')
