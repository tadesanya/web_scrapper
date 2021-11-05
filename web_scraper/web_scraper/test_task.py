from .task import get_source, HTMLSession, scrape_google, create_filename, google_search

TEST_URL_QUERY = 'https://www.google.co.uk/search?q=test+data'
SEARCH_QUERY = 'test data'


def test_get_source(mocker):

    session_get = mocker.patch.object(HTMLSession, 'get')
    result = get_source(TEST_URL_QUERY)

    session_get.assert_called_with(TEST_URL_QUERY)


def test_scrape_google(mocker):
    get_source_mock = mocker.patch('web_scraper.task.get_source')
    get_source_mock.html.find.return_value = ""
    scrape_google(SEARCH_QUERY, 12)

    get_source_mock.assert_called


def test_create_filename():
    result = create_filename()
    assert isinstance(result, str)
    assert result.split('.')[1] == 'txt'
