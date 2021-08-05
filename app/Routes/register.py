from flask import render_template, flash, redirect, url_for
from app import app
from flask_login import current_user
from app.Models.User import User
from app import db
from app.Forms.Registration_Form import RegistrationForm

from flask import Blueprint

from app.Models.User import User

register_blue = Blueprint('register', __name__)

#注册
@register_blue.route('/register', methods=['GET', 'POST'])
def register():
    # 判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, user_id= current_user.id)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你成为我们网站的新用户!')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)