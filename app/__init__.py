from flask import Flask
from flask_pymongo import PyMongo

# Initialize PyMongo
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/usersdb'  # MongoDB URI
    mongo.init_app(app)  # Initialize MongoDB with Flask app

    # Register Blueprints
    from .routes import user_routes
    app.register_blueprint(user_routes)  # Register the user_routes blueprint

    return app
