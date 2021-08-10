from flask import redirect, url_for
from app import app
from flask_login import logout_user

from flask import Blueprint

from app.Models.User import User

from app.Routes import bp

#退出登录
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.index'))