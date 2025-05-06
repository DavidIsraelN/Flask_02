from app.repositories.prize_repository import fetch_prize_data

def get_all_categories():
    data = fetch_prize_data()
    categories = {prize['category'] for prize in data.get('prizes', [])}
    return sorted(categories)
