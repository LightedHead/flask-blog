from flask import render_template
from app import app
from flask_login import login_required
from app.Models.User import User

#个人信息的留言
@app.route('/user/<username>')
@login_required
def user(username):

    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author':user,'body':'测试Post #1号'},
        {'author':user,'body':'测试Post #2号'}
    ]

    return render_template('user.html',user=user,posts=posts)