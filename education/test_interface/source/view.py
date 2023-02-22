from flask import Blueprint

view = Blueprint('view', __name__)


@view.route('/')
def index():
    return "<h1>TEST TITLE</h1>"
