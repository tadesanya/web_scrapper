import requests
import urllib
from requests_html import HTMLSession
from datetime import datetime


def get_source(url):
    """Return the source code for the provided URL.

    Args:
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query, number_of_result):
    """Returns links gotten from query search"""
    query = urllib.parse.quote_plus(query)

    # account for missing 2 results if number of requested results greater than 10
    number_of_result = number_of_result + 2 if number_of_result > 10 else number_of_result
    response = get_source("https://www.google.co.uk/search?q=" + query + "&num=" + str(number_of_result))

    selection_query = 'div.g > div > div > div > a'
    links = response.html.find(selection_query)

    return links


def create_filename():
    """Returns a filename concatenated with the datetime"""
    timestamp = datetime.now()
    return "result_{0}{1}{2}{3}{4}{5}.txt".format(timestamp.year, timestamp.month, timestamp.day,
                                                  timestamp.hour, timestamp.minute, timestamp.second)
