# pylint: disable=missing-docstring,line-too-long
import sys
from os import path

def parse(html):
    pass # TODO: return a list of dict {name, prep_time, cooking_time}

def write_csv(ingredient, recipes):
    pass # TODO: dump recipes to a CSV file `recipes/INGREDIENT.csv`

def scrape_from_internet(ingredient, start=0):
    pass # TODO: Use `requests` to get the HTML page of search results for given ingredients.

def scrape_from_file(ingredient):
    file = f"pages/{ingredient}.html"
    if path.exists(file):
        return open(file)
    print("Please, run the following command first:")
    print(f'  curl "http://www.letscookfrench.com/recipes/find-recipe.aspx?aqt={ingredient}" > pages/{ingredient}.html')
    sys.exit(1)

def main():
    if len(sys.argv) > 1:
        ingredient = sys.argv[1]
        # TODO: Replace scrape_from_file with scrape_from_internet and implement pagination (5 pages needed)
        recipes = parse(scrape_from_file(ingredient))
        write_csv(ingredient, recipes)
    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)

if __name__ == '__main__':
    main()
