## Data Cleaning 🧹

### Motivation 

Being able to clean a dataset and quickly explore it crucial for a succesful data science project. 

In this exercise, you will perform an exploratory analysis and load data in a Python class which would come handy when we will need to access our data. 

### 🔥 Warm-up

- Make sure to follow the setup steps and that you are able to run: 

```python
from olist.data import Olist
Olist().ping()
```

### Load data

- Download 9 csv files from the Kaggle Olist page [here](https://www.kaggle.com/olistbr/brazilian-ecommerce). Place them under the file `data/`
- Run `jupyter notebook` and open `data_cleaning` file. 
- Write a script to load all dataset in a dictionary named data, where each key is the name of the csv file.

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

- *get_data()*: that will return all data as a dictionnary where each key contains each DataFrame. Your DataFrame should then contains the following keys: 

```python
['olist_sellers_dataset', 'product_category_name_translation',
  'olist_orders_dataset', 'olist_order_items_dataset',
  'olist_customers_dataset', 'olist_geolocation_dataset',
  'olist_order_payments_dataset', 'olist_order_reviews_dataset',
  'olist_products_dataset']
```

- *get_matching_table()*: that will return a DataFrame with the following columns: `customer_id`, `customer_unique_id`, `order_id`, `product_id`, `seller_id`. Only returns data for orders that are `delivered`.
  
- Make sure you can import and inspect data from a notebook, by running: 
  
  ```python
  from olist.data import Olist 
  olist = Olist()
  data = olist.get_data()
  matching_table = olist.get_matching_table()
  ```