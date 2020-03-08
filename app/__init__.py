"""
程序工厂函数的目的: 延迟创建Flask应用， 应用场景如下:
     1). 测试。可以使用多个应用程序的实例，为每个实例分配分配不同的配置， 从而测试每一种不同的情况。
     2). 多个实例。要同时运行同一个应用的不同版本，可以在你的Web服务器中配置多个实例并分配不同的配置.

"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager


from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
# session_protection 属性提供不同的安全等级防止用户会话遭篡改。
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面的端点。
login_manager.login_view = 'auth.login'

def create_app(config_name='development'):
    """
     默认创建开发环境的app对象
     """
    app = Flask(__name__)
    """
    config = {
       'development': DevelopmentConfig,
       'testing': TestingConfig,
       'production': ProductionConfig,
       'default': DevelopmentConfig
    }

    """
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 3). 注册蓝图，和app关联在一起
    from app.auth import auth
    app.register_blueprint(auth)
    from app.todo import  todo
    app.register_blueprint(todo, url_prefix='/todo')
    return  app



