from flask import Blueprint, jsonify
from app.services.prize_service import get_all_categories

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
