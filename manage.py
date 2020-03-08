"""
File: manage.py.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""
from app import create_app, db

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app.models import Role, User

app = create_app()
manager = Manager(app)
# 将数据库迁移插件与数据库db和app关联
migrate = Migrate(app, db)


@manager.command
def tests():
    """
    执行Flask项目的测试用例
    """
    import unittest
    # 发现所有的测试用例(TestCase)绑定成一个测试集合(TestSuite), TestLoader
    tests = unittest.TestLoader().discover('tests')
    # verbosity是测试结果的信息复杂度，有0、1、2 三个值
    unittest.TextTestRunner(verbosity=2).run(tests)


def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)


if __name__ == '__main__':
    # app = create_app()
    # # 0.0.0.0: 0代表任意，
    # # 绑定本机的所有IP， http://IP:8888
    # app.run(host='0.0.0.0', port='8888')

    # 初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。
    # 当交互式环境python manage.py shell,自动传入参数/变量: app, db, Role,User
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command("db", MigrateCommand)

    manager.run()
