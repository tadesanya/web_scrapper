import requests
import urllib
from requests_html import HTMLSession
from datetime import datetime

MAX_RESULT_PER_PAGE = 10


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
    response_links = []
    query = urllib.parse.quote_plus(query)
    number_of_pages, remaining_result_size = divmod(number_of_result, MAX_RESULT_PER_PAGE)
    query_start_point = 0

    # loop through all the pages needed for the number of results desired, except the final page
    selection_query = 'div.g > div > div > div > a'
    for page_number in range(0, number_of_pages):
        response = get_source("https://www.google.co.uk/search?q=" + query + "&num=" + str(MAX_RESULT_PER_PAGE)
                              + "&start=" + str(query_start_point))
        links = response.html.find(selection_query)
        response_links.extend(links)
        query_start_point += 10

    # Get search results for final page
    final_response = get_source("https://www.google.co.uk/search?q=" + query + "&num=" + str(remaining_result_size)
                                + "&start=" + str(query_start_point))
    final_links = final_response.html.find(selection_query)
    response_links.extend(final_links)

    return response_links


def create_filename():
    """Returns a filename concatenated with the datetime"""
    timestamp = datetime.now()
    return "result_{0}{1}{2}{3}{4}{5}.txt".format(timestamp.year, timestamp.month, timestamp.day,
                                                  timestamp.hour, timestamp.minute, timestamp.second)
