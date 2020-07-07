If you managed to complete all the challenges of the day so far, congratulations!

Let's finish the day with a kind of **advanced scraping**. In this challenge we'll be using a _real_ browser. You will see that this technique can be used to perform **web automation** (like submitting forms for instance!)

Some websites don't work the way HTTP & HTML were intended to work. They use a technique called **client-side rendering** where the HTML starts almost empty, and all the DOM on the page is generated thanks to JavaScript.

This means that if you use the traditional technique where you look into the HTML (`curl`-style), you won't find anything! You need the JavaScript to be fully rendered, and to do so you need a browser, like Chrome.

To drive Chrome from code, you need a pilot. We will use [**Selenium**](https://www.seleniumhq.org/). Thank to it, you can navigate to a page, scroll down, click on a link, fill a few inputs, click on a button, etc. Anything a human can do with a browser can be done with Selenium.

⚠️ There is no `make` on this challenge.

## Example

Imagine you want to get some information about a rental car. The URL structure is easy to understand:

```bash
https://uk.getaround.com/car-hire/roissy-en-france/chevrolet-aveo-545062
```

Go to [that URL](https://uk.getaround.com/search?address=CDG+-+Paris+Charles+de+Gaulle+Airport&address_source=poi&poi_id=210&latitude=49.0128&longitude=2.55&city_display_name=&start_date=&start_time=&end_date=&end_time=&country_scope=FR&car_sharing=true&user_interacted_with_car_sharing=false), disable JavaScript in your browser, and reload. To disable JS quickly you can install those extensions:

- [Disable JavaScript](https://addons.mozilla.org/en-US/firefox/addon/disable-javascript/) for Firefox 🦊
- [Disable JavaScript](https://chrome.google.com/webstore/detail/disable-javascript/jfpdlihdedhlmhlbgooailmfhahieoem) for Chrome 🎈

See how the page loads indefinitely? We can't scrape with just `requests` + `BeautifulSoup` from the server-side generated HTML, we need Selenium and a browser!

## Setup

For this challenge, we will use Selenium + Chrome. If you want to try another browser (Firefox), you can do that as well but the instructions will need to be adapted.

Open Google Chrome on your computer (if you don't have it, install it), then go to "About Google Chrome". You should see the version you are on (Maybe 78? More?).

Based on that version, install the right [`chromedriver-binary`](https://pypi.org/project/chromedriver-binary/77.0.3865.40.0/#history) and [`selenium`](https://pypi.org/project/selenium/) modules:

```bash
pip install selenium
pip install chromedriver-binary==77.0.3865.40.0 # Version might be different!
```

OK! Now that this is done, open the `test_advanced_scraping.py` file and copy/paste the following code:

```python
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("https://uk.getaround.com/")

# driver.quit()
```

Open your terminal and run:

```bash
python test_advanced_scraping.py
```

🚀 It should open a Chrome Window, navigate to the page and stay like that! If you uncomment the last line `driver.quit()` then you will see that Chrome will close automatically. You need to do that otherwise you'll have plenty of Chrome Windows opened after a while!

## Searching cars in Paris Charles de Gaulle Airport

We will now simulate a user interaction with the page. Something one can do is click on the search bar and type a location. Go ahead and try it: type `CDG - Paris Charles de Gaulle Airport`. You should see a popup opening with some suggestions. Now click on `CDG - Paris Charles de Gaulle Airport` and click on the big `Search` button to launch the search.

This is what we want to emulate! We will use the [`find_element_by_id`](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id) method to locate the input in which we want to type.

```python
from selenium.webdriver.common.keys import Keys

search_input = driver.find_element_by_id('TODO') # Open the inspector in Chrome and find the input id!
search_input.send_keys('CDG - Paris Charles de Gaulle Airport')
```

With that piece of code you should see your Chrome browser opening on the specified URL and filling the location input with `CDG - Paris Charles de Gaulle Airport`

## Submitting the form

This is where it starts to become tricky. If we try to just submit on the form, we will get an error message from the website saying we need to select one of the proposed suggestions in the popup. You may notice that the suggestions take some time to actually load. THis means that we can't select one of those suggestions right away after filling the input with a location. We have to wait for the suggestions to load.

This means we need to use an [**explicit wait**](https://selenium-python.readthedocs.io/waits.html):

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# [...]
wait = WebDriverWait(driver, 15)
wait.until(ec.visibility_of_element_located((By.XPATH, "//li[@id='-1291973610']")))
```

The weird string uses an [XPath](https://en.wikipedia.org/wiki/XPath) search in the DOM. It locates the `<li/>` with an `id` which has the value `-1291973610`. After exploration of GetAround's DOM, we found that this `<li/>` is the `CDG - Paris Charles de Gaulle Airport` suggestion. We're then left with two things to do. Click on the suggestion and submit the form.

```python
suggestion = driver.find_element_by_id('-1291973610')
suggestion.click()
search_input.submit()
```

Copy the code above and run your script. You should see that the search form is submitted and you are redirected to the search results. You may notice that the results are also loaded using Javascript so we have to follow the same technique as before. After inspecting the DOM of the page, we can see that the results are all listed inside a `<div/>` with two classes.

```html
<div class="js_picks_results_container picks_results_container">
<!-- ... -->
</div>
```

We will use the same technique as before and we will wait for this HTML element to appear in the DOM to actually gather the URLS of all the cars listed on that page

```python
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='js_picks_results_container picks_results_container']")))
```

Then it's a matter of looping over each result. GetAround's HTML is not too bad to parse. We can see that each card representing a car is an `<a/>` tag with two classes

```html
<a href="..." class="car_card_revamp js_picks_car_card"></a>
```

This means we can write the following code:

```python
car_urls = []
cards = driver.find_elements_by_xpath("//a[@class='car_card_revamp js_picks_car_card']")
print(f"Found {len(cards)} results on the page")
for card in cards:
    url = card.get_attribute('href')
    car_urls.append(url)
print(car_urls)
```

Run the code from the terminal. You should get a list of urls printed.

## Scraping each place

Now that we have a list of urls, we can now navigate to each page, and give it to BeautifulSoup to gather the data we need!

For each car, the following code will gather:

- The name of the car
- The year of the car
- the owner name
- the price to rent the car

We start with an empty list `cars` that we will populate with `dict` storing information about each car:


```python
from bs4 import BeautifulSoup

# [...]

cars = []
for url in car_urls:
  print(f"Navigating to {url}")
  driver.get(url)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  name = soup.find('h1', class_='car_info_header__title').string.strip()
  year = soup.find('span', class_='car_info_header__attributes').text.strip().split()[0]
  owner_name = soup.find(class_='car_owner_section').find(class_='link_no_style js_drk_lnk').string.strip()
  price = soup.find(class_='js_default_price').find(class_='cobalt-text-titleLarge').text.strip()
  cars.append({
    'name': name,
    'year': year,
    'owner': owner_name,
    'price': price
  })
```

Finally we can save the results in a csv file using the techniques we learned earlier during the day:

```python
import csv

with open('data/cars.csv', 'w') as file:
  writer = csv.DictWriter(file, fieldnames=cars[0].keys())
  writer.writeheader()
  writer.writerows(cars)

driver.quit()
```

## Going Headless

Launching a web scraping script with Selenium opens a Google Chrome window which goes in the way and prevent you from doing something else (you might have seen that interacting with the page using the mouse or keyboard while the script is running breaks it). There's a solution for that: [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome). The idea is to use Chrome without its user interace. This is how you can do it:

Replace this line:

```python
driver = webdriver.Chrome()
```

With the following lines:

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

Add a few `print()` statements (as you won't see what's going on anymore!) and re-start:

```python
python test_advanced_scraping.py
```
