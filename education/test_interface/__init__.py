from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Orion123'

    from .source.auth import auth
    from .source.view import view
    from .source.afisha import afisha

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(afisha, url_prefix='/')

    return app
