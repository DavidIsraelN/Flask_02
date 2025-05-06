from flask import Blueprint, jsonify, request
from app.services.country_service import get_country_code

country_bp = Blueprint('countries', __name__)


# Route to fetch country code by country name (getting the country name from the query string)
@country_bp.route('/code', methods=['GET'])
def fetch_country_code():
    try:
        country_name = request.args.get('country_name')
        if not country_name:
            return jsonify({'error': 'Missing country parameter'}), 400
        country_code = get_country_code(country_name)
        if not country_code:
            return jsonify({'error': f'Country "{country_name}" not found'}), 404
        print(f"Fetched country code for {country_name}: {country_code}")  # Debugging line to check fetched country code
        return jsonify({'country': country_name, 'code': country_code}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
