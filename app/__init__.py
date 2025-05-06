from flask import Flask
from app.routes.prize_routes import prize_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints for ex01, ex02, ex03 from the presentation
    # to get all categories from the Nobel Prize API click on http://localhost:5000/prizes/categories
    # to get all names of the Nobel Prize winners click on http://localhost:5000/prizes/names
    # to get the top category in the Nobel Prize click on http://localhost:5000/prizes/top-category
    app.register_blueprint(prize_bp, url_prefix='/prizes')
    
    return app
