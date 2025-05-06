from flask import Flask
from app.routes.prize_routes import prize_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints for ex01 from the presentation
    # to get all categories from the Nobel Prize API click on http://localhost:5000/prizes/categories
    app.register_blueprint(prize_bp, url_prefix='/prizes')
    
    return app
