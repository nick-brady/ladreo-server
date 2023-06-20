from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize extensions
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Blueprints registration
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app