from flask import Flask
from app.routes.prize_routes import prize_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints for ex01, ex02, ex03, ex04 from the presentation
    # to get all categories from the Nobel Prize API click on http://localhost:5000/prizes/categories
    # to get all names of the Nobel Prize winners click on http://localhost:5000/prizes/names
    # to get the top category in the Nobel Prize click on http://localhost:5000/prizes/top-category
    # to get categories by year you can for example to click on http://localhost:5000/prizes/categories-by-year?year=1923 (you can change the year to any year you want)
    app.register_blueprint(prize_bp, url_prefix='/prizes')
    
    return app
