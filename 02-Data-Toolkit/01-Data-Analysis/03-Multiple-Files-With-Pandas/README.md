It's very common that the data we need is scattered around many files, especially CSVs. Or it could be that it's in one file but in multiple worksheets. So far we have been using the [`pandas.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function which is straightforward: give it a CSV, and it will create a dataframe with all columns and rows found in the CSV.

When you have multiple files, it's a bit different. Sure you can load 10 files into 10 different dataframes, but what if you want to **reconciliate** the data? Welcome to the wonderful world of **Pandas Merging**.

## Context & Documentation

Pandas provides three functions to "add" two dataframes:

- [`pandas.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
- [`pandas.DataFrame.merge()`](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.merge.html)
- [`pandas.DataFrame.join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)


Everything is explained in the [Merge, join and concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) article of the documentation, still it's a _very_ (very!) long article that can't really be read at once hoping to understand/remember everything.

## A bit of Theory

Before we load actual CSVs and try to merge/join/concatenate them, we are going to work with Dataframes created from dictionaries. This will limit the amount of data we manipulate and will make the concepts easier to understand.

**Create a new notebook** in this exercise folder and start with the usual following `import` as the first cell:

```python
import numpy as np
import pandas as pd
import matplotlib
```

Then let's create a first DataFrame storing information about Countries picked up on Google:

```python
a_df = pd.DataFrame({
    'Country': ['Germany', 'France', 'Belgium', 'Finland'],
    'Population (M)': [82.8, 67.2, 11.4, 5.5],
    'Capital': ['Berlin', 'Paris', 'Brussels', 'Helsinki']
})
a_df
```

Let's suppose we now have a table of [HDI](https://en.wikipedia.org/wiki/Human_Development_Index), in a new cell:

```python
b_df = pd.DataFrame({
    'Country': ['Germany', 'France', 'Belgium', 'Canada'],
    'HDI': [0.936, 0.901, 0.916, 0.926]
})
b_df
```

### Inner Merge

Try to [**`merge`**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) `a_df` and `b_df`. Read the documentation for the function, especially about the `on` parameter. Which option should it be? Just pass this argument, and no others, what can you say about Canada? Finland?

<details><summary markdown='span'>View solution
</summary>

We are merging on the **Country** column! Here's the code to do it:

```python
inner_merged_df = a_df.merge(b_df, on='Country')
inner_merged_df
```

We just performed an **inner** merge, meaning that we **only** kept the rows for which, for each value of the `Column` row, there is a row in both `a_df` and `b_df`.

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/inner_ugz2wa.png)

In our example, the `a_df` has a line about `Finland` but `b_df` does not, so this row is not included in the inner merge. Same thing for `Canada`, it's present in `b_df` but not in `a_df` so it's not present in the inner merge.

This line of code is equivalent to:

```python
a_df.merge(b_df, on='Country', how='inner')
```

</details>

### Left Merge

There are four possible merges, the previous section covered the _inner_ merge. Let's try to do the **left** merge:

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/left_jrs58n.png)

Create a new cell and build the `left_merged_df` variable. What do you see? What about `Finland`? `Canada`?

<details><summary markdown='span'>View solution
</summary>

```python
left_merged_df = a_df.merge(b_df, on='Country', how='left')
left_merged_df
```

We can see in the `left_merged_df` that **all the rows from `a_df`** have been preserved, whether or not the country was present in the `b_df`. That's why the HDI for `Finland` is [`NaN`](https://docs.scipy.org/doc/numpy/user/misc.html). The country `Canada` which is **not** in the `a_df` gets ignored.

</details>

### Right Merge

You probably get where we are going now. We just did a _left_ merge, so now let's have a look at the **right** merge!

![](https://res.cloudinary.com/wagon/image/upload/v1562058696/right_lm5ivj.png)

Same idea, create a new cell and build the `right_merged_df` variable. What do you see? What about `Finland`? `Canada`?

<details><summary markdown='span'>View solution
</summary>

```python
right_merged_df = a_df.merge(b_df, on='Country', how='right')
right_merged_df
```

This time, as it's a **right** merge, all the `b_df` rows are kept, regardless of the data found in `b_df`. That's why we can find a column for `Canada` with the HDI specified, but no population and no Capital!

</details>

### Outer Merge

Finally, there is a merge which will keep **all** the rows from both `a_df` and `b_df`, the **outer** merge.

![](https://res.cloudinary.com/wagon/image/upload/v1562058696/outer_q76gh9.png)

Add a new cell and test it:

```python
outer_merged_df = a_df.merge(b_df, on='Country', how='outer')
outer_merged_df
```

You can see that we have 5 rows, and `Finland` and `Canada` are both present! `NaN` is used when there is missing data for a column not found. Like for the Titanic dataset, you can quickly have an overview of how "full" each column is:

```python
outer_merged_df.info()
```

:information_source: Pandas has a whole article in the documentation about [Working with missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html). Again it's a pretty long article that you don't need to read now, but keep it in mind next time you are exploring a Dataset with a lot of `NaN`.

---

### Join

The `merge` function was useful to merge based on a given **column**. We will now see another use case where you want to merge based on the **index** (the rows). First, let's create two new dataframes `aa_df` and `bb_df`.

```python
aa_df = a_df.set_index("Country")
aa_df
```

```python
bb_df = b_df.set_index("Country")
bb_df
```

Let's now use [`pandas.DataFrame.join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html):

```python
aa_df.join(bb_df)
```

:question: What's your conclusion? Was it a left, right, inner or outer join?

<details><summary markdown='span'>View solution
</summary>

By default, `.join()` does a **left** join. Try the other types of join:

```python
aa_df.join(bb_df, how='inner')
aa_df.join(bb_df, how='right')
aa_df.join(bb_df, how='outer')
```

</details>

:question: You see that `.merge()` and `.join()` give the same outcome in the end. So when should you use one or the other?

<details><summary markdown='span'>View solution
</summary>

You can use `.merge()` when you want to merge based on a given **column** and `.join()` when you want to join on the **index**.

</details>

---

### Concat

There's a third way to put two dataframes together, using [`pandas.concat()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html). Let's jump right into it:

```python
concat_df = pd.concat([a_df, b_df], axis="index", sort=False)
concat_df
```

This method is a bit more "dumb", it just combines the two dataframes into one by **stacking** their rows. This might prove useful in some situations though, so it's worth to know how to use it.

---

## Loading data from multiple CSVs

To practice loading multiple CSVs and merging them, we're going to use the [Olympic Sports and Medals, 1896-2014](https://www.kaggle.com/the-guardian/olympic-games) which contains 3 files:

- `dictionary.csv`
- `summer.csv`
- `winter.csv`

Note, that the files are located in the _same folder_ as the notebook you are working on.

Go ahead and write the code to load `dictionary.csv` into the DataFrame `countries_df`:

<details><summary markdown='span'>View solution
</summary>

```python
countries_df = pd.read_csv('dictionary.csv')
countries_df.head()
```

</details>


Now load the CSV of **Summer** Games in a `summer_df` dataframe. On which column should we merge `countries_df` and `summer_df`? Do they have the same name? If not, use the [`pandas.DataFrame.rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) function.

<details><summary markdown='span'>View solution
</summary>

```python
summer_df = pd.read_csv('summer.csv')
summer_df.rename(columns={"Country": "Code"}, inplace=True)
summer_df.head()
```

</details>

Do the same for **Winter** Games in a `winter_df` dataframe.

<details><summary markdown='span'>View solution
</summary>

```python
winter_df = pd.read_csv('winter.csv')
winter_df.rename(columns={"Country": "Code"}, inplace=True)
winter_df.head()
```

</details>

### Merging the data

Time to perform a merge of `countries_df` and `summer_df` (into a new DataFrame `summer_countries_df`). As we'll want to merge all games into one DataFrame at the end, **add a `Season`** column to the `summer_countries_df`.

<details><summary markdown='span'>View solution
</summary>

```python
summer_countries_df = summer_df.merge(countries_df, on="Code")
summer_countries_df["Season"] = "Summer"
summer_countries_df.head()
```

</details>

Repeat the same approach to create a `winter_countries_df`.

<details><summary markdown='span'>View solution
</summary>

```python
winter_countries_df = winter_df.merge(countries_df, on="Code")
winter_countries_df["Season"] = "Winter"
winter_countries_df.head()
```

</details>

Concatenate `summer_countries_df` and `winter_countries_df` (they have the same columns!) into an `all_df` DataFrame.


<details><summary markdown='span'>View solution
</summary>

```python
all_df = pd.concat([summer_countries_df, winter_countries_df], sort=False)
all_df.head()
```

</details>

### Top 10 Countries since 1984

Use boolean indexing, grouping & sorting to create a new dataframe consisting of the Top 10 countries who won the most medals _since 1984_. Save it in the `top_10_df` variable. Then plot it. Go step by step!

<details><summary markdown='span'>View solution
</summary>

```python
all_count_df = all_df[all_df["Year"] >= 1984] \
    .groupby(["Country"]) \
    .count()[["Medal"]] \
    .sort_values(by="Medal", ascending=False)
top_10_df = all_count_df.head(10)
```

To plot the result with a barchart you can do:

```python
top_10_df.plot(kind="bar")
```

</details>


### Test your code

Add a new **markdown** cell:

```markdown
### Check your code
```

and then the code to persist your variables:

```python
from nbresult import ChallengeResult

result = ChallengeResult('olympic_games',
    summer_countries_shape=summer_countries_df.shape,
    all_countries_shape=all_df.shape,
    top_country_1=top_10_df.iloc[0]['Medal'],
    top_country_10=top_10_df.iloc[9]['Medal'],
)
result.write()
```

You can now check the correctness of your code with:

```python
print(result.check())
```


### Optional - Top 10 Countries (by Season) since 1984

Let's reuse `all_df` to group but this time we don't just want to count the total number of medals for each country, we want to count the number of medals for Winter Games on the one hand, and for Summer Games on the other hand. Then we want to plot them (sorting should still be based on the _total_ number of medals).

:bulb: **Hint 1** The [`pandas.DataFrame.groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) can group over a **`list`** of columns.

:bulb: **Hint 2** You need to use the [`pandas.DataFrame.unstack()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html) function


<details><summary markdown='span'>View solution
</summary>

Let's build the Top 10 with two columns: Winter & Summer

```python
season_count_df = all_df[all_df["Year"] >= 1984].groupby(["Country", "Season"])["Medal"].count().unstack()
season_count_df.fillna(0, inplace=True)
season_count_df["Summer"] = season_count_df["Summer"].astype(int)
season_count_df["Winter"] = season_count_df["Winter"].astype(int)
season_count_df.head(10)
```

As we need to sort the season_count_df based on the **Total** number of medals, we need to add a third column to `season_count_df` like this:

```python
season_count_df["Total"] = all_count_df
season_count_df.head(10)
```

And now we are ready to plot!

```python
season_count_df.sort_values(by="Total", ascending=False)[["Summer", "Winter"]].head(10).plot(kind="bar")
```

</details>
