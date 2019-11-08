### About Olist 🇧🇷

![olist](https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png)

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers from inventory management, dealing with reviews and customer contacts to logistic services.

Olist charge sellers a monthly fee. This fee is progressive with the volume of orders.

Remember the seller and customer workflows:

**Seller:**
- Seller join Olist
- Seller upload product catalogue
- Seller get notified when a product is sold.
- Seller hand over item to logistic carrier.

👉 Note that multiple sellers can be involved in one customer order!

**Customer:**
- Browse products on marketplaces
- Purchase products from Olist.store
- Get an expected date for delivery
- Customer Receive order
- Customer leave a review for the order

👉 A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

### Dataset

The dataset consists of 8 csv files that can be downloaded on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

You have access to information (customer, seller, product, reviews..) of 100k orders from 2016 and 2018 that were made on Olist store.

More information can be found on [Olist dataset documentation](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data) or on the original Kaggle page.


### Setup

To get started, make sure to complete the two steps below:

**1 - Edit your PYTHONPATH**

- Add `07-Best-Practices` path to your `PYTHONPATH`. This will help us easily import our modules throughout the class.

On Mac:

```bash
open ~/.bashrc
export PYTHONPATH="/Users/<user.github_nickname>/repos/data-challenges/07-Best-Practices:$PYTHONPATH"
```

For Windows:

- `System Properties > Advanced> Environment Variables.`
- Locate the Variable name `PYTHONPATH`
- Add your path `C:\path\to\07-Best-Practices`

**2 - Install required packages**

- Install needed python packages with the command:

```python
pip install -r ../../requirements-best_practices.txt
```

### Motivation

Being able to clean a dataset and quickly explore it is crucial for a successful data science project.

In this exercise, you will perform an **exploratory analysis** and load data in a Python class which would come handy when we will need to access our data.

### 🔥 Warm-up

- Make sure to follow the setup steps and that you are able to run:

```python
from ...olist.data import Olist
Olist().ping()
```

### Load data

- Download 9 csv files from the Kaggle Olist page [here](https://www.kaggle.com/olistbr/brazilian-ecommerce). Place them under the `data-challenges/07-Best-Practices/data/` folder
- Run `jupyter notebook` and open the `data_cleaning.ipynb` file.
- Write a script to load all datasets in a dictionary named `data`, where each key is the name of the csv file.

👉 Hint: you can use the `os` library to navigate files in Python

### Pandas Profiling

- Run an exploratory analysis for the list of datasets below. Use [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling) to output one HTML output per dataset under a `report` folder. You can limit your analysis to those tables:

```python
['olist_orders_dataset', 'olist_products_dataset', 'olist_customers_dataset', 'olist_order_reviews_dataset', 'olist_order_items_dataset']
```

- Challenge: in the file `data_cleaning.py` add the columns that have missing data and columns that should be converted to datetime.

- Why are some rows of the column `order_delivered_customer_date` null? How would you filter the `order` dataset moving forward?
- Which columns should be converted as datetime?

### Olist Class

- Challenge: within the `olist/data.py` file, implement two methods:

- *get_data()*: that will return all data as a dictionnary where each key contains each DataFrame. Your DataFrame should then contain the following keys:

```python
['olist_sellers_dataset', 'product_category_name_translation',
  'olist_orders_dataset', 'olist_order_items_dataset',
  'olist_customers_dataset', 'olist_geolocation_dataset',
  'olist_order_payments_dataset', 'olist_order_reviews_dataset',
  'olist_products_dataset']
```

- `get_matching_table()`: that will return a DataFrame with the following columns: `customer_id`, `customer_unique_id`, `order_id`, `product_id`, `seller_id`. Only return data for orders that are `delivered`.

- Make sure you can import and inspect data from a notebook, by running:

```python
from ...olist.data import Olist
olist = Olist()
data = olist.get_data()
matching_table = olist.get_matching_table()
```
