from flask import redirect, url_for
from app import app
from flask_login import logout_user

from flask import Blueprint

from app.Models.User import User

logout_blue = Blueprint('logout', __name__)

#退出登录
@logout_blue.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))