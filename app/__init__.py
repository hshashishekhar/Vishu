from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create the SQLAlchemy db object
db = SQLAlchemy()

# Create the LoginManager object
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the db with the app
    db.init_app(app)

    # Initialize the login_manager with the app
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Set the login view

    # Add the user_loader callback
    from .models import User  # Import the User model

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app