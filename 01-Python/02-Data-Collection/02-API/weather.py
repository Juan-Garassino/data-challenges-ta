# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

def search_city(query):
    '''Look for a given city and disambiguate between several candidates'''
    pass # TODO(implement this method)

def weather_forecast(woeid):
    '''Returns a 5-element list of weather forecast for a given woeid'''
    pass # TODO(implement this method)

def main():
    '''Ask user for a city and display weather forecast'''
    pass # TODO(implement this method)


# You should not need to touch the code below:
if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
