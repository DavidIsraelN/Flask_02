from flask import Blueprint, jsonify, request
from app.services.prize_service import get_all_categories, get_all_names, get_categories_by_year, get_top_category

prize_bp = Blueprint('prizes', __name__)


# Route to fetch all categories
@prize_bp.route('/categories', methods=['GET'])
def fetch_categories():
    try:
        categories = get_all_categories()
        if not categories:
            return jsonify({'error': 'No categories found'}), 404
        print(f"Fetched categories: {categories}")  # Debugging line to check fetched categories
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Route to fetch all names of the Nobel Prize winners
@prize_bp.route('/names', methods=['GET'])
def fetch_names():
    try:
        names = get_all_names()
        print(f"Fetched names: {names}")  # Debugging line to check fetched names
        # print("Fetched categories:")  # Debugging line to check fetched names
        # for name in names:
        #     print(f"    {name['first_name']} {name['last_name']}")
        return jsonify(names), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to fetch the top category in the Nobel Prize
@prize_bp.route('/top-category', methods=['GET'])
def fetch_top_category():
    try:
        top_category = get_top_category()
        print(f"Fetched top category: {top_category}")  # Debugging line to check fetched top category
        return jsonify({'top_category': top_category}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Route to fetch categories by year (getting the year from the query string)
@prize_bp.route('/categories-by-year', methods=['GET'])
def fetch_categories_by_year():
    try:
        year = request.args.get('year')
        if not year or not year.isdigit():
            return jsonify({'error': 'Invalid or missing year parameter'}), 400
        categories = get_categories_by_year(int(year))
        if not categories:
            return jsonify({'error': 'No categories found for the given year'}), 404
        print(f"Fetched categories for year {year}: {categories}")  # Debugging line to check fetched categories by year
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500