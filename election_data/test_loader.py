from .loader import get_pollster_from_url


def test_get_pollster_emnid():
    url = 'https://www.wahlrecht.de/umfragen/emnid.htm'
    pollster = get_pollster_from_url(url)

    assert pollster == 'emnid'
