from flask import Flask
# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# 登录插件
from flask_login import LoginManager

app = Flask(__name__)

app._static_folder = "./templates/static"

# 添加配置信息
app.config.from_object(Config)

# 建立数据库关系
db = SQLAlchemy(app)
# 绑定app和数据库，以便进行操作
migrate = Migrate(app, db)

login = LoginManager(app)

# 有一部分功能是要你登录后才能使用的，那么在flask中怎么实现这个登录才能使用的功能呢？
login.login_view = 'login'
from app.Routes import *
from app.Models import *

from app.Routes.to_index import to_index_blue
from app.Routes.login import login_blue
from app.Routes.register import register_blue
from app.Routes.logout import logout_blue
from app.Routes.article_operation import article_operation_blue
from app.Routes.edit_profit import edit_profit_blue

app.register_blueprint(login_blue)
app.register_blueprint(to_index_blue)
app.register_blueprint(register_blue)
app.register_blueprint(logout_blue)
app.register_blueprint(article_operation_blue)
app.register_blueprint(edit_profit_blue)
