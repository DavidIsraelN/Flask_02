import requests

API_URL = "https://api.nobelprize.org/v1/prize.json"

def fetch_prize_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
