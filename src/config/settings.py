# config/settings.py

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
import os
from dotenv import load_dotenv
from flasgger import Swagger
from flask_login import LoginManager



# Load environment variables
load_dotenv()

# Initialize the database and migration objects (but don't attach them to the app yet)
db = SQLAlchemy()
migrate = Migrate()
seeder = FlaskSeeder()

def create_app(settings_conf=None):
    """Application factory to create a Flask app instance."""
    app = Flask(__name__)

    # Swagger configuration for securityDefinitions
    swagger_config = {
        "swagger": "2.0",
        "title": "babycyle API",
        "description": "API documentation of babycyle backend e-commerce",
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": 'JWT Authorization header using the Bearer scheme. Example: "Bearer {token}"'
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ],
        # Include the 'specs' key to resolve KeyError
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",  # URL for accessing the Swagger UI
        # Add a headers key to prevent TypeError
        "headers": []
    }
   
    # Load configuration
    swagger = Swagger(app, config=swagger_config)

    os.environ.setdefault("FLASK_SETTINGS_MODULE", "src.config.prod")
    conf = settings_conf or os.getenv("FLASK_SETTINGS_MODULE")
    app.config.from_object(conf)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI_PROD')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['DEBUG'] = os.getenv('DEBUG', 'True') == 'True'  # Convert from string to boolean
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'YourFallbackSecretKey')

    # app.config['DEBUG'] = True

    # Initialize the app with extensions
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)

    # login_manager = LoginManager(app)
    # # login_manager.login_view = "/"  # Set the login view endpoint name

    # @login_manager.user_loader
    # def load_user(user_id):
    #     from src.model.user import User
    #     return User.query.get(int(user_id))

    api_url='/api/v1'
    from src.routers.auth import auth_bp
    app.register_blueprint(auth_bp, name='authentication', url_prefix=api_url + '/auth')



    
    @app.route('/')
    def hello_from_api():
        return 'Mad API v2'
    
    @app.route('/create-all-db')
    def create_all_db():
        db.create_all()
        return jsonify({'message': 'Database created successfully'})
    
    return app