## Goal

Being able to clean a dataset and quickly explore it is crucial for a successful data science project.

In this exercise, you will perform an **Exploratory Data Analysis** (EDA) and load data in a Python class which would come handy when we need to access our data throughout the week.

Reminder: Full dataset documentation is available [here](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data)

## 🔥 Warm-up

Go to the `olist` folder and run an `ipython` session:

```bash
cd ~/code/<user.team_lead_github_nickname>/olist
```

Then type the following to check that the setup phase from the previous exercise worked:

```python
from olist.data import Olist
Olist().ping()
# => pong
```

If you get something else than `pong`, raise a ticket to get some help from a TA.

### Load data

Download 9 csv files from the Kaggle Olist page [here](https://www.kaggle.com/olistbr/brazilian-ecommerce). Place them in the `data/csv` folder.

Run `jupyter lab` and open the `notebooks/01_02_data_cleaning.ipynb` file. Follow instructions within.

### Pandas Profiling

Run an exploratory analysis for the list of datasets below using [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling). If you don't have it yet in your virtualenv you can get it with:

```bash
pip install pandas-profiling
```

### Olist Class

Challenge: within the `olist/data.py` file, implement two methods:

- `get_data()`
- `get_matching_table()`

Make sure you can import and inspect data from a notebook using those two methods.
