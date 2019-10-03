## Foreword

One usualy source of data is API. Those can be [public API](https://github.com/public-apis/public-apis) with auth or not, free or paying, those can be internal APIs at your company, etc.

When it comes to API, there are some keywords to know about:

- [SOAP](https://en.wikipedia.org/wiki/SOAP) (old)
- [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) (current)
- [GraphQL](https://en.wikipedia.org/wiki/GraphQL) (very new, less frequent)
- [XML](https://en.wikipedia.org/wiki/XML) (old)
- [JSON](https://en.wikipedia.org/wiki/JSON) (current)

The first three keywords refer to a **protocol** on top of HTTP(s) and is really important to figure out as you want to **consume** data from an API.

The two last keywords refer to a **data format** that would usually be sent back to you when performing an API call.

ℹ️ Most modern APIs are RESTful and send JSON. In this challenge, we are going to use such an API.

## Reading the documentation

When presented with a new API to use, your first reflex should be to go straight to the documentation, and figure out the following:

1. Is this a REST API?
1. Does it serve JSON?
1. Is this API authenticated? (do I need to sign up to get an API key? do I need to pay?)
1. What is the base URI?
1. What endpoints can I call? What data do they return?

👯‍♂️ Buddy time! Go to [metaweather.com](https://www.metaweather.com/), find the documentation, read it, and try answering those questions. When you are comfortable with what this API is about, you can start working on the challenge

## Making a test call to the API

Before building something fancy, we need to make sure that we can run a first API call successfully. This is a sanity check to make sure we don't start coding too much before realizing that the API we intended to use is not a good fit.

So how should make our first call? There are several options:

### Using the browser

The browser _is_ an HTTP client! If there are no complex request `Header` to set and the verb to use is `GET`, then it's just as easy as typing the URL in the address bar. Try it!

Open a new browser tab, and copy paste the following URL:

```bash
https://www.metaweather.com/api/location/search/?query=london
```

What do you see? If you are on Chrome, you should install the [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) extension for a prettier look. In the end, JSON is just text that needs to be **parsed**, that's what the extension will do

### Using Postman

[Postman](https://www.getpostman.com/) is an app that many developers download on their laptop to use when building software consuming APIs. It provides a more advanced experience where you need to a fine control over:

- HTTP Verb (`GET`, `POST`, `PATCH`, `DELETE`, etc.)
- Request headers (`Content-Type`, `Authorization`, etc.)
- Request body (`application/x-www-form-urlencoded` or `raw`)

This application allow to **save** some requests, has tabs and more advanced feature. Try it!

### Using Python

Finally, we want to use this API in _our code_. Python's standard library comes with a [`http.client`](https://docs.python.org/3/library/http.client.html) built-in module, but we are not going to use it. Instead, we are going to use the [`requests`](https://requests.readthedocs.io) library, an 'elegant and simple HTTP library for Python, built for human beings'.

Open the `test_api.py` file and paste the following code:

```python
import requests

url = "https://www.metaweather.com/api/location/search/?query=london"
response = requests.get(url).json()
city = response[0]
print(f"{city['title']}: {city['woeid']} ({city['latt_long']})")
```

Save and run the following command:

```bash
python test_api.py
```

Is it working? Did you grab successfully London's woeid? Some questions for you to answer with your buddy before moving forward:

1. Line `4`, why are we chaining a `.json()` after `.get()`? Does it still work without that call? You can `print()` intermediate steps to convince yourself. (💡 [Doc](https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content))
1. Line `5`, why do we do `[0]`? What's the type of `response`?
1. Line `6`, what's the type of `city['woeid']`, `str` or `int`? Why?

To answer those questions, don't hesitate to `print()` or **even better**, [debug](https://pypi.org/project/ipdb/). This first week is a good time to sharpen your debugging skills before diving into more advanced topics.

## Let the challenge begin!

### Weather CLI

Let's build a weather [CLI](https://en.wikipedia.org/wiki/Command-line_interface) using the API. Here's the flow for a user (pseudo-code!):

1. Launch `python weather.py`
1. Get asked to type a city name
1. If city is unknown to the API, display an error message and get back to step 2.
1. If user input is ambiguous (several cities comes back from search), display them and ask the user to pick one. (💡 Hint: there's a built-in [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) that might be useful)
1. Fetch weather forecast for the next 5 days and display it (Date, Weather and max temperature in °C)
1. Go back to step 2 (loop to ask for a new city).
1. At any point, `Ctrl`-`C` will take care of quitting the program

In action, it will should look like this:

<iframe src="https://player.vimeo.com/video/364146887" width="640" height="480" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

Open the `weather.py` file. You will be greated by three empty method:

1. `search_city(query)`
1. `weather_forecast(woeid)`
1. `main()`

You need to implement them, in that order. The `./check.sh` will assist you for the first two methods, and for the last one you will need to run the Python program directly with `python weather.py`.

Good luck!

### History

TODO


