
from app import app

from flask import redirect, url_for

@app.route('/')
def toindex():
    return redirect(url_for('blog.index'))