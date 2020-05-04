If you managed to complete all the challenges of the day so far, congratulations!

Let's finish the day with a kind of **advanced scraping**, one using a _real_ browser. You will see that this technique can be even used to perform **web automation** (like submitting forms for instance!)

Some websites don't work the way HTTP & HTML were invented. They use a technique called **client-side rendering** where the HTML starts almost empty, and all the DOM on the page is generated thanks to JavaScript.

This means that if you go with the traditional technique where you look into the HTML (`curl`-style), you won't find anything! You need the JavaScript to be fully rendered, and to do so you need a browser, like Chrome.

To drive Chrome from code, you need a pilot. We will use [**Selenium**](https://www.seleniumhq.org/). Thank to it, you can navigate to a page, scroll down, click on a link, fill a few inputs, click on a button, etc. Anything a human can do with a browser can be done with Selenium.

⚠️ There is no `make` on this challenge.

## Example

Imagine you want to get some information about an Airbnb place. The URL structure is easy to understand:

```bash
https://www.airbnb.com/rooms/3993887
```

Go to [that URL](https://www.airbnb.com/rooms/3993887), disable JavaScript in your browser, and reload. To disable JS quickly you can install those extensions:

- [Disable JavaScript](https://addons.mozilla.org/en-US/firefox/addon/disable-javascript/) for Firefox 🦊
- [Disable JavaScript](https://chrome.google.com/webstore/detail/disable-javascript/jfpdlihdedhlmhlbgooailmfhahieoem) for Chrome 🎈

See how the DOM is empty? We can't scrape with just `requests` + `BeautifulSoup` from the server-side generated HTML, we need Selenium and a browser!

## Setup

For this challenge, we will use Selenium + Chrome. If you want to try another browser (Firefox), you can too but the instructions will need to be adapted.

Open Google Chrome on your computer (if you don't have it, install it), then go to "About". You should see the version you are on (Maybe 78? More?).

Based on that version, install the right [`chromedriver-binary`](https://pypi.org/project/chromedriver-binary/77.0.3865.40.0/#history) and [`selenium`](https://pypi.org/project/selenium/) modules:

```bash
pip install selenium
pip install chromedriver-binary==77.0.3865.40.0 # Version might be different!
```

OK then open the `test_advanced_scraping.py` file and copy/paste the following code:

```python
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("https://www.airbnb.com/s/homes")

# driver.quit()
```

Open your terminal and run:

```bash
python test_advanced_scraping.py
```

🚀 It should open a Chrome Window, navigate to the page and stay like that! If you uncomment the last line `driver.quit()` then you will see that Chrome will close automatically. You need to do that otherwise you'll have plenty of Chrome Windows opened after a while!

## Going to Bali

We will now simulate a user interaction with the page. Something one can do is click on the top left search bar and type a country or a city. Go ahead and try it: type `Bali` then the `Enter` key. You should be redirected to a list of results.

This is what we want to emulate! We will use the [`find_element_by_id`](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id) method to locate the input in which we want to type.

```python
from selenium.webdriver.common.keys import Keys

search_input = driver.find_element_by_id('TODO') # Open the inspector in Chrome and find the input id!
search_input.send_keys('Bali')
search_input.send_keys(Keys.ENTER)
```

## Gathering search results URLs

It starts to become tricky. You may have noticed that the results take some time to actually load. This means that we can't gather straight away after having typed the `Keys.ENTER` as the list of places is not fully loaded yet.

This means we need to use an [**explicit wait**](https://selenium-python.readthedocs.io/waits.html):

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# [...]
wait = WebDriverWait(driver, 15)
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@itemprop='itemListElement']")))
```

The weird string uses an [XPath](https://en.wikipedia.org/wiki/XPath) search in the DOM. It locates the `<div />` with an attribute `itemprop` which has the value `itemListElement`. After exploration of Airbnb's DOM, we found that this `<div />` contains all the results.

Then it's a matter of looping over each result. Airbnb's HTML is quite hard to parse, there's no proper class names as they use an advanced React technique for CSS. This means there's not much to which we can bind our code to. Still we managed to find that each result has a `<meta itemprop='url'>` tag which allow us to gather the room ids from the results.

```html
<div itemprop="itemListElement">
  <meta itemprop="name" content="Tropical Suite Villa private pool 5 - undefined - Canggu">
  <meta itemprop="position" content="1">
  <meta itemprop="url" content="www.airbnb.com/rooms/5749962?previous_page_section_name=1000">
  <!-- [...] --%>
</div>
```

This means we can write the following code:

```python
import re

room_ids = []
cards = driver.find_elements_by_xpath("//meta[@itemprop='url']")
print(f"Found {len(cards)} results on the page")
for card in cards:
    url = card.get_attribute('content')
    result = re.search('/rooms/(\d+)', url)
    if result:
        room_ids.append(int(result.group(1)))

print(room_ids)
```

Run the code from the terminal. You should get a list of ids printed.

💡 Notice that the `re` package allows us to perform a regular expression with group extraction on the attribute `content`.

## Scraping each place

Now that we have a list of ids, and knowing the URL structure of a specific place (see first section "Example"), we can now navigate to each page, wait for the HTML to load (AJAX...) and give it to BeautifulSoup!

For each flat, the following code will gather:

- The name of the flat
- The available amenities

We start with an empty list `flats` that we will populate with `dict` storing information about each flat:


```python
from bs4 import BeautifulSoup

flats = []

for room_id in room_ids: # If you want to test only on 2 flats, run it on `room_ids[:2]`
    url = f"https://www.airbnb.com/rooms/{room_id}"
    print(f"Navigating to {url}")
    driver.get(url)

    wait = WebDriverWait(driver, 15)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@itemprop='name']//h1")))

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    name = soup.find('h1').text.strip()
    amenities_cells = soup.select('#amenities table td')
    amenities = [a for a in map(lambda x: x.text, amenities_cells) if a and 'Unavailable' not in a]

    flats.append({
        'room_id': room_id,
        'name': name,
        'amenities': amenities
    })
```

Finally we can display the results on the screen like that:

```python
import json

print("---------------- RESULTS ----------------------")
print(json.dumps(flats, indent=4))
```

## Going Headless

Launching a web scraping script with Selenium opens a Google Chrome window which goes in the way and prevent you from doing something else (you might have seen that interacting with the page with the mouse or keyboard while the script is running breaks it). There's a solution for that: [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome). The idea is to use Chrome without its user interace. This is how you can do it:

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
