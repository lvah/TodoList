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
    PER_PAGE = 2

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
    """
    QQ邮箱:  MAIL_PORT=465 MAIL_USE_SSL=True
    163邮箱: MAIL_PORT=25  MAIL_USE_SSL=False(默认不开启)
    """
    MAIL_SERVER = 'smtp.qq.com'  # 邮件服务器
    MAIL_PORT = 465  # 邮件服务器的端口
    MAIL_USE_SSL = True
    MAIL_USERNAME = '976131979@qq.com'  # 发送者邮箱账户
    MAIL_PASSWORD = 'mganldfowzitbdcj'  # 授权密码而不是登录密码
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
