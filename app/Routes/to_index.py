from app import db, login
from app import app
from datetime import datetime
from flask_login import current_user, login_required
from app.Forms.Post_Form import PostForm
from flask import render_template

from flask import Blueprint

from app.Models.User import User

to_index_blue = Blueprint('to_index', __name__)

@to_index_blue.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

#建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@to_index_blue.route('/')
@to_index_blue.route('/index')
@login_required  #这样，必须登录后才能访问首页了,会自动跳转至登录页
def index():
    user = {'username': 'Bobs BuBu'}
    posts = [
        {
            'author': {'username': '徐'},
            'body': '这是模板模块中的循环例子～1'

        },
        {
            'author': {'username': '吴迪'},
            'body': '这是模板模块中的循环例子～2'
        }
    ]
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        publish_date = datetime.now()
        print(title)
        print(text)
        print(publish_date)

    return render_template('index.html',title = '我的',user = user,posts = posts)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))