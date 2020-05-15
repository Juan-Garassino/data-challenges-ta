## Goal

Being able to clean a dataset and quickly explore it is crucial for a successful data science project.

In this exercise, you will perform an **Exploratory Data Analysis** (EDA) and load data in a Python class which would come handy when we need to access our data throughout the week.

### Data Schema

Your challenge is to build the data schema of olist using [db.lewagon.org](db.lewagon.org). Don't forget to quick-save it regularily ("F2") to your kitt profile.

Notice that we have written for you in `csv/README.md` a detailed description of the data schema. The `.md` format (called "markdown") is better viewed on github. On your fork or direclty in lewagon upstream repository [here](https://github.com/lewagon/data-challenges/tree/master/04-Decision-Science/data)

### Exploratory Data Analysis with Jupyter

Let's get real!

Open your `data_cleaning.ipynb` notebook and follow instructions within.

### Coding Olist Class
Once you are satisfied with your analysis on jupyter notebook, good practice is to copy a clean version of your analysis into your committed code base.

Within the `olist/data.py` file, implement two methods:

- `get_data()`
- `get_matching_table()`

Make sure you can import them back from any notebook or ipython session as follows

```python
from olist.data import Olist
Olist().get_matching_table()
```
