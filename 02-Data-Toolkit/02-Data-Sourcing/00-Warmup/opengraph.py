# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    response = requests.get("https://opengraph.lewagon.com", params={'url': url})
    if response.status_code != 200:
        return None
    return response.json()["data"] # Returns the ["data"] because the response has a dict with the key "data"

if __name__ == "__main__":
    # To manually test, please uncomment the following lines and run `python opengraph.py`:
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(fetch_metadata("https://www.lewagon.com"))
