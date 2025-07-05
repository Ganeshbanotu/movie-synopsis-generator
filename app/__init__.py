from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'devsecret')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.models import User  # 👈 Required for user_loader

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth_bp.login'

    from app.routes import main
    from app.auth import auth_bp

    app.register_blueprint(main)
    app.register_blueprint(auth_bp)

    return app
