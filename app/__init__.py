from flask import Flask
from app.routes.prize_routes import prize_bp
from app.routes.country_routes import country_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints for *ex01, ex02, ex03 and ex04* from the presentation
    # to get all categories from the Nobel Prize API click on http://localhost:5000/prizes/categories
    # to get all names of the Nobel Prize winners click on http://localhost:5000/prizes/names
    # to get the top category in the Nobel Prize click on http://localhost:5000/prizes/top-category
    # to get categories by year, you can for example to click on http://localhost:5000/prizes/categories-by-year?year=1923 
    #                                                                       (you can change the year to any year you want)
    app.register_blueprint(prize_bp, url_prefix='/prizes')

    # Register blueprints for *ex05* from the presentation
    # to get the country code for a given country name, you can click on http://localhost:5000/countries/code?country_name=israel 
    #                                                                   (you can change the country name to any country you want)
    app.register_blueprint(country_bp, url_prefix='/countries')
    
    return app
