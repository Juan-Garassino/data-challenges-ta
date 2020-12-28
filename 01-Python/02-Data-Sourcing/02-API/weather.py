# pylint: disable=missing-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    # TODO: Look for a given city and disambiguate between several candidates. Return one city (or None)
    pass


def weather_forecast(woeid):
    # TODO: Return a 5-element list of weather forecast for a given woeid
    pass


def main():
    query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
