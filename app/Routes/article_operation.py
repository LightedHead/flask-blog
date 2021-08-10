from flask import render_template, redirect, url_for, request
from app import app
from app.Forms.Post_Form import PostForm
from flask_login import login_required
from app.Models.Aricle import  Article
from app import db
from datetime import datetime

from app.Routes import bp

#文章的创建
@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_article():
    """View function for new_port."""
    form = PostForm()

    if form.validate_on_submit():
        new_post = Article(title=form.title.data, body= form.text.data,)

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.index'))

    return render_template('new_article.html',form=form)

#文章的编辑
@bp.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    """View function for edit_post."""

    #一对多查询
    post = Article.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = id
        post.body = form.text.data
        post.timestamp = datetime.now()

        # Update the post
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.edit_article', id=post.title))

    form.title.data = post.title
    form.text.data = post.body
    return render_template('edit_article.html', form=form, post=post)

#查看文章列表
@bp.route('/my_article', methods=['GET', 'POST'])
@login_required
def my_article():

    article = Article.query.all()

    return render_template('my_article.html', article=article)

#文章的删除
@bp.route('/delete_article/<string:id>', methods=['GET', 'POST'])
@login_required
def delete_article(id):
    """View function for edit_post."""

    #一对多查询
    post = Article.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.my_article'))

    return render_template(url_for('blog.my_article'))

#文章的查找
@bp.route('/search_article', methods=['GET', 'POST'])
@login_required
def search_article():
    """View function for edit_post."""

    title = str(request.form.get('content'))
    title_article = Article.query.get_or_404(title)
    searched = 1

    return render_template('my_article.html', title_article=title_article,searched = searched)