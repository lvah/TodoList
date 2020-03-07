import os

# 获取当前项目的绝对路径;
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    所有配置环境的基类, 包含通用配置
    """
    # 尤其是涉及(flask-wtf)登录注册里面提交敏感信息时，一定要加
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'westos secret key'
    # flask-sqlchemy
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[TodoList]'
    FLASKY_MAIL_SENDER = '976131979@qq.com'

    @staticmethod
    def init_app(app):
        """
        初始化app，当前不用， 后续完善， 用来添加第三方插件的
        :param app:
        :return:
        """
        pass


class DevelopmentConfig(Config):
    """
   开发环境的配置信息
   """
    # 启用了调试支持,服务器会在代码修改后自动重新载入,并在发生错误时提供一个相当有用的调试器。
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '976131979'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '密码'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """
   测试环境的配置信息
   """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    """
   生产环境的配置信息
   """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
   'development': DevelopmentConfig,
   'testing': TestingConfig,
   'production': ProductionConfig,
   'default': DevelopmentConfig
}

