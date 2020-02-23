### Motivation

Being able to clean a dataset and quickly explore it is crucial for a successful data science project.

In this exercise, you will perform an **exploratory analysis** and load data in a Python class which would come handy when we will need to access our data.

Reminder: Full dataset documentation is available [here](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data)

### 🔥 Warm-up

- Make sure to follow the setup steps and that you are able to run:

```python
from olist.data import Olist
Olist().ping()
```

### Load data

- Download 9 csv files from the Kaggle Olist page [here](https://www.kaggle.com/olistbr/brazilian-ecommerce). Place them under a `olist/data/csv` folder
- Run `jupyter notebook` and open the `01_02_data_cleaning.ipynb` file and follow the instructions

### Pandas Profiling

- Run an exploratory analysis for the list of datasets below using [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling) (make sur to pip install pandas-profiling)

### Olist Class

Challenge: within the `olist/data.py` file, implement two methods:
- `get_data()`
- `get_matching_table()`
- Make sure you can import and inspect data from a notebook
