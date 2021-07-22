#从app模块中即从__init__.py中导入创建的app应用
from uuid import uuid4

from flask import render_template, flash, redirect, url_for,request
from app import app
#导入表单处理方法
from forms import LoginForm, PostForm

from flask_login import current_user, login_user
from app.models import User, Post, load_user, article
from flask_login import logout_user
from flask_login import login_required

from app import db
from forms import RegistrationForm

from datetime import datetime
from forms import EditProfileForm

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

#建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
@app.route('/index')
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

@app.route('/login',methods=['GET','POST'])
def login():
    # 判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    #创建一个表单实例
    form = LoginForm()
    # 对表格数据进行验证
    if form.validate_on_submit():
        # 根据表格里的数据进行查询，如果查询到数据返回User对象，否则返回None
        user = User.query.filter_by(username=form.username.data).first()
        # 判断用户不存在或者密码不正确
        if user is None or not user.check_password(form.password.data):
            # 如果用户不存在或者密码不正确就会闪现这条信息
            flash('无效的用户名或密码')
            # 然后重定向到登录页面
            return redirect(url_for('login'))
        # 这是一个非常方便的方法，当用户名和密码都正确时来解决记住用户是否记住登录状态的问题
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='登录', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
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

@app.route('/user/<username>')
@login_required
def user(username):

    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author':user,'body':'测试Post #1号'},
        {'author':user,'body':'测试Post #2号'}
    ]

    return render_template('user.html',user=user,posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('你的提交已变更.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='个人资料编辑',
                           form=form)

#文章的创建
@app.route('/new', methods=['GET', 'POST'])
@login_required
def new_article():
    """View function for new_port."""
    form = PostForm()

    if form.validate_on_submit():
        new_post = article(title=form.title.data, body= form.text.data)

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_article.html',
                           form=form)

#文章的编辑
@app.route('/edit/<string:id>', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    """View function for edit_post."""

    post = Post.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish_date = datetime.now()

        # Update the post
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_id=load_user(id)))

    form.title.data = post.title
    form.text.data = post.text
    return render_template('edit_article.html', form=form, post=post)

@app.route('/edit/<string:id>', methods=['GET', 'POST'])
@login_required
def list_article(id):
    """View function for edit_post."""

    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        publish_date = datetime.now()
        print(title)
        print(text)
        print(publish_date)

        return redirect(url_for('index'))


    return render_template('edit_article.html', form=form, post=post)
