from flask import Flask, request, jsonify,render_template, redirect, url_for,session,message_flashed,send_file,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
db = SQLAlchemy()
app = Flask(__name__)
def create_app():
    """Construct the core application."""
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    with app.app_context():
        from .portfolio.portfolio import portfolio
        app.register_blueprint(portfolio)
        db.create_all()
        return app
