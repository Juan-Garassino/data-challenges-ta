import pandas as pd
import numpy as np
import math
from olist.data import Olist
from olist.order import Order


class Review:

    def __init__(self):
        # Import only data once
        olist = Olist()
        self.data = olist.get_data()
        self.matching_table = olist.get_matching_table()
        self.order = Order()

    def get_training_data(self):
        """
        04-02 > Returns a DataFrame with:
       'review_id', 'order_id', 'review_comment_length', 'product_category'
        """
