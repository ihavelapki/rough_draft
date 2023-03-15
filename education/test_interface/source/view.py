from flask import Blueprint, render_template

view = Blueprint('view', __name__)


@view.route('/')
def index():
    return render_template("home.html")
