import pandas as pd
import numpy as np
from olist.data import Olist
from olist.order import Order


class Product:

    def __init__(self):
        # Import only data once
        olist = Olist()
        self.data = olist.get_data()
        self.matching_table = olist.get_matching_table()
        self.order = Order()

    def get_product_features(self):
        """
        Returns a DataFrame with:
       'product_id', 'product_category_name', 'product_name_length',
       'product_description_length', 'product_photos_qty', 'product_weight_g',
       'product_length_cm', 'product_height_cm', 'product_width_cm'
        """

        products = self.data['products']

        # (optional) convert name to english
        en_category = self.data['product_category_name_translation']
        df = products.merge(en_category, on='product_category_name')
        df.drop(['product_category_name'], axis=1, inplace=True)
        df.rename(columns={'product_category_name_english': 'category'},
                  inplace=True)


        return df

    def get_price(self):
        """
        Return a DataFrame with:
        'product_id', 'price'
        """

        products = self.data['products']
        order_items = self.data['order_items']
        return products[['product_id']].merge(order_items[['product_id', 'price']], on='product_id')

    def get_wait_time(self):
        """
        Returns a DataFrame with:
        'product_id', 'wait_time'
        """
        matching_table = self.matching_table
        orders_wait_time = self.order.get_wait_time()

        df = matching_table.merge(orders_wait_time,
                                 on='order_id')

        return df.groupby('product_id',
                          as_index=False).agg({'wait_time': 'mean'})

    def get_review_score(self):
        """
        Returns a DataFrame with:
        'product_id', 'share_of_five_stars', 'share_of_one_stars',
        'review_score'
        """
        matching_table = self.matching_table
        orders_reviews = self.order.get_review_score()

        # Since same products can appear multiple times in the same
        # order, create a product <> order matching table

        matching_table = matching_table[['order_id',
                                         'product_id']].drop_duplicates()
        df = matching_table.merge(orders_reviews,
                                  on='order_id')

        def cost_of_reviews(s):
            ''' evaluate the cost for olist of a series of reviews '''
            sum = 0
            for x in s:
                if x == 1:
                    sum += 100
                if x == 2:
                    sum += 50
                if x == 3:
                    sum += 40
            return sum

        df['review_score_copy'] = df['review_score']
        df = df.groupby('product_id',
                        as_index=False).agg({'dim_is_one_star': 'mean',
                                             'dim_is_five_star': 'mean',
                                             'review_score': 'mean',
                                             'review_score_copy': cost_of_reviews
                                             })
        df.columns = ['product_id', 'share_of_one_stars',
                      'share_of_five_stars', 'review_score', 'cost_of_reviews']

        return df

    def get_quantity(self):
        """
        Returns a DataFrame with:
        'product_id', 'n_orders', 'quantity'
        """
        matching_table = self.matching_table

        n_orders =\
            matching_table.groupby('product_id')['order_id'].nunique().reset_index()
        n_orders.columns = ['product_id', 'n_orders']

        quantity = \
            matching_table.groupby('product_id',
                                   as_index=False).agg({'order_id': 'count'})
        quantity.columns = ['product_id', 'quantity']

        return n_orders.merge(quantity, on='product_id')

    def get_training_data(self):

        training_set =\
            self.get_product_features()\
                .merge(
                self.get_wait_time(), on='product_id'
               ).merge(
                self.get_price(), on='product_id'
               ).merge(
                self.get_review_score(), on='product_id'
               ).merge(
                self.get_quantity(), on='product_id'
               )

        return training_set

    def get_product_cat(self, agg="mean"):
        '''
        Returns a DataFrame aggregating various properties for each product 'category',
        using the aggregation function passed in argument.
        The 'quantity' columns refers to the total number of product sold for this category.
        '''
        product_cat = self.get_training_data().groupby("category").agg(
            {
                "review_score": agg,
                "share_of_one_stars": agg,
                "share_of_five_stars": agg,
                "wait_time": agg,
                "price": agg,
                "product_weight_g": agg,
                "product_length_cm": agg,
                "product_height_cm": agg,
                "product_width_cm": agg,
                "product_photos_qty": agg,
                "n_orders": agg,
                "quantity": "sum",
                "cost_of_reviews": "sum"
            }
        )
        return product_cat
