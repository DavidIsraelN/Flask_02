from app.repositories.prize_repository import fetch_prize_data


def get_all_categories():
    data = fetch_prize_data()
    categories = {prize['category'] for prize in data.get('prizes', [])}
    return sorted(categories)


def get_all_names():
    data = fetch_prize_data()
    names = []
    for prize in data.get('prizes', []):
        for laureate in prize.get('laureates', []):
            first_name = laureate.get('firstname', '')
            last_name = laureate.get('surname', '')
            if first_name or last_name:
                names.append({'first_name': first_name, 'last_name': last_name})
    return names