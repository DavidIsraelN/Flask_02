import requests

BASE_API_URL = "https://api.nobelprize.org/v1/" 
URL_COUNTRY = BASE_API_URL + "country.json"
URL_PRIZE = BASE_API_URL + "prize.json"


def fetch_data(url):
    """
    Fetches data from the given URL.
    Raises an HTTPError for bad responses (4xx and 5xx).
    Returns the JSON response.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_country_data():
    return fetch_data(URL_COUNTRY)

def fetch_prize_data():
    return fetch_data(URL_PRIZE)
