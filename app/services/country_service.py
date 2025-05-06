from app.repositories.nobel_repository import fetch_country_data


def get_country_code(country_name):
    """
    Fetches the country code for a given country name from the Nobel Prize API.
    Returns the country code if found, otherwise returns None.
    """
    data = fetch_country_data()
    for country in data.get('countries', []):
        if country.get('name').lower() == country_name.lower():
            return country.get('code')
    return None
