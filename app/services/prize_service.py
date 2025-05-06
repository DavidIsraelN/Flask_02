from typing import Counter
from app.repositories.nobel_repository import fetch_prize_data


def get_all_categories():
    """
    Fetches all categories from the Nobel Prize API.
    Returns a sorted list of unique categories.
    """
    data = fetch_prize_data()
    categories = {prize['category'] for prize in data.get('prizes', [])}
    return sorted(categories)


def get_all_names():
    """
    Fetches all names of the Nobel Prize winners from the API.
    Returns a list of dictionaries, each containing the first and last name of a laureate.
    """
    data = fetch_prize_data()
    names = []
    for prize in data.get('prizes', []):
        for laureate in prize.get('laureates', []):
            first_name = laureate.get('firstname', '')
            last_name = laureate.get('surname', '')
            if first_name or last_name:
                names.append({'first_name': first_name, 'last_name': last_name})
    return names


def get_top_category():
    """
    Fetches the top category in the Nobel Prize.
    Returns the category with the highest number of prizes awarded.
    """
    data = fetch_prize_data()
    categories = [prize['category'] for prize in data.get('prizes', [])]
    category_counter = Counter(categories)
    top_category = category_counter.most_common(1)
    return top_category[0][0] if top_category else None


def get_categories_by_year(year):
    """
    Fetches categories for a specific year from the Nobel Prize API.
    Returns a sorted list of unique categories for that year.
    """
    data = fetch_prize_data()
    categories = {
        prize['category']
        for prize in data.get('prizes', [])
        if prize.get('year') == str(year)
    }
    return sorted(categories)
