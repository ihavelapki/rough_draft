from os import path
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager
from config import DB_NAME

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.instance_path = path.join(path.dirname(__file__), 'data')
    app.config.from_object(config)
    db.init_app(app)

    from .source.auth import auth
    from .source.view import view

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, UserInfo

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_load(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists(path.join(app.instance_path, DB_NAME)):
        with app.app_context():
            db.create_all()
        print('DB created')


