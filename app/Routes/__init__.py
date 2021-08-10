from flask import Blueprint

bp = Blueprint('blog', __name__, template_folder='../templates')

from app.Routes import article_operation, edit_profit, login, logout, register, to_index, user_sayings