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
login.login_view = 'blog.login'
from app.Routes import *
from app.Models import *

from app.Routes import bp

app.register_blueprint(bp)
