print('view')
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from education.authserver import db
from education.authserver.models import User, UserInfo

view = Blueprint('view', __name__)


def get_use_info(user_id):
    print('inside get user_info:', user_id)
    user_info = UserInfo.query.filter_by(user_id=user_id).first()
    print(user_info.user_id)
    print(user_info.first_name)
    return user_info


@view.route('/')
@login_required
def index():
    print('id user in index func', current_user.id)
    user_info = get_use_info(current_user.id)
    return render_template("home.html", user=current_user, user_info=user_info)
