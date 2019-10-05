Web Scraping is the last solution one need to use to automate data retrieval and there is _no API_ at disposal. This technique is actually the one used by Google to build its index for the famous Search Engine. The Google bot performing this action is called a [crawler](https://www.google.com/search/howsearchworks/crawling-indexing/).

In the Python world, scraping means importing [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), a library to pull data out of HTML.

## Example

We are going to srape the Recipe directory [letscookfrench.com](http://www.letscookfrench.com/recipes/)

Open the `test_scraping.py` file in a text editor and paste the following code:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("pages/carrot.html"), "html.parser")

for city in soup.find_all('div', {'class' : 'm_titre_resultat'}):
    print(city.text)
```

In your terminal, now run:

```bash
python test_scraping.py
```

💣 OK, you got an error. Can you read it? What are you missing?

What we want to do here is called **offline scraping**. While developing the scraper, we don't want to send an HTTP requests to the server everytime we run the code. We'll take the risk of spamming the site, get detected and _banned_.

Let's download the search results for the keyword `carrot`:

```bash
curl "http://www.letscookfrench.com/recipes/find-recipe.aspx?aqt=carrot" > pages/carrot.html
```

Now, run the Python script once again:

```bash
python test_scraping.py
```

✨ Congrats! You've just scraped your first page.

## Challenge

The goal of this challenge is to write a Python script that will parse the first 50 recipes for a given keyword and store them into the `recipes` folder. It should work like this:

```bash
python recipe.py chocolate

ls -lh recipes
# -rw-r--r--  12K  chocolate.csv

head -n 3 recipes/chocolate.csv

# name,prep_time,cooking_time
# Chocolate Truffles,30 min,
# Mini Chocolate Fondants,10 min,12 min
```

In order to get to this final result, there are a few functions to implement in `recipe.py`

- `parse(html)`: this is the most important function. It needs to locate every recipe on the page, and dive into the `<div />` of a given recipe to locate its name, cooking time and preparation time (optional, some recipes don't have it). After exploring the DOM, it will return a `list` of `dict` containing 3 keys (`name`, `prep_time`, `cooking_time`).
- `write_csv(ingredient, recipes)`: this method takes two parameters. The first one is a `str`, the second one a `list` of `dict`. It will create a CSV file `{ingredient}.csv` and store the recipes fro mthe list `recipes` (the code for that function should be 90% the same as the code from the previous challenge `02-API`). You can already launch `python recipe.py cucumber` to test the CSV is being created.
- `scrape_from_internet(ingredient, start)`: this method will go on the website and search for the given `ingredient`. Ignore the `start` parameter to begin with. It should return the HTML from the page (to be fed to the `parse` method)
- `main()` Update the method so that `scrape_from_internet` is called instead of `scrape_from_file`. Run a few tests like `python recipe.py chocolate` or `python recipe.py strawberry`. After each run, check the `recipes` folder and open the created CSV file. Does it look OK to you?
- `main()` with **pagination**: you now need to update the `main` and the `scrape_from_internet` functions so that the program does not stop at the first page of search results but download 50 recipes!

🙌 Have fun scraping!
