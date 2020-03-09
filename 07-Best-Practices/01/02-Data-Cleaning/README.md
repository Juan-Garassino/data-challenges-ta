## Goal

Being able to clean a dataset and quickly explore it is crucial for a successful data science project.

In this exercise, you will perform an **Exploratory Data Analysis** (EDA) and load data in a Python class which would come handy when we need to access our data throughout the week.

Reminder: Full dataset documentation is available [here](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data)

### 🔥 Warm-up

We now work in your local olist foler.

Go to the `olist` folder and run an `ipython` session:

```bash
cd ~/code/<user.team_lead_github_nickname>/olist/notebooks
ipython
```

Then type the following to check that the setup phase from the previous exercise worked:

```python
from olist.data import Olist
Olist().ping()
# => pong
```

If you get something else than `pong`, raise a ticket to get some help from a TA. You might have a problem with the `$PYTHONPATH`.

### Exploratory analysis on Jupyter Notebook

Download 9 csv files from the Kaggle Olist page [here](https://www.kaggle.com/olistbr/brazilian-ecommerce). Place them in your local `data/csv` folder.

Open the `notebooks/01_02_data_cleaning.ipynb` file and follow instructions within.

### Coding Olist Class
Once you are satisfied with your analysis on jupyter notebook, standard practice is to copy a clean version of your analysis into your committed code base.

Challenge: within the `olist/data.py` file, implement two methods:

- `get_data()`
- `get_matching_table()`

Make sure you can import and inspect data from a notebook using those two methods.
