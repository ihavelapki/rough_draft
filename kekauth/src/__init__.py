# print('src init:', __name__, __file__)
from os import path
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app(config):
    # print('create app', __name__, __file__)
    app = Flask(__name__)
    # app.instance_path = path.join(path.dirname(__file__), 'data')
    app.config.from_object(config)
    db.init_app(app)
    # print('create app before import bp', __name__, __file__)
    from .route.auth import auth
    from .route.home import home
    # print('create app after import bp', __name__, __file__)
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from kekauth.data import Users

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_load(id):
        return Users.query.get(int(id))

    return app


def create_db(app):
    if not path.exists(path.join(app.instance_path, app.config['DB_NAME'])):
        with app.app_context():
            db.create_all()
        print('DB created')