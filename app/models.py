"""
File: models.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description:

设计数据库模型:
    1). 用户信息： User
    2). 用户角色信息: Role
    3). 用户角色: 用户 = 1:n, 一对多关系，外键写在多的一端。

login_manager回调函数的作用:
    注册回调函数， 当没有session_id时， 通过装饰器指定的函数来读取用户到sesion中， 达到前端可通过current_user获取当前用户的目的
"""
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin

# Flask中一个Model子类就是数据库中的一个表。默认表名'User'.lower() ===> user
"""
user = User(username="westos")
user.password = 'westos123'
user.password
"""


class User(UserMixin, db.Model):
    """
    因为继承了UserMixin类， 自动继承里面的属性和方法：
    Flask-Login 提供了一个 UserMixin 类,包含常用方法的默认实现,且能满足大多数需求。
        1). is_authenticated    用户是否已经登录?
        2). is_active           是否允许用户登录?False代表用户禁用
        3). is_anonymous        是否匿名用户?
        4). get_id()            返回用户的唯一标识符

    """
    __tablename__ = 'users'  # 自定义数据表的表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    # 外键关联
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        # generate_password_hash(password, method= pbkdf2:sha1 , salt_length=8):密码加密的散列值。
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # check_password_hash(hash, password) :密码散列值和用户输入的密码是
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User: %s>" % (self.username)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # 做了两件事情: 1). Role添加属性users    2). User添加属性role
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role: %s>" % (self.name)


# 后续用户登录和注销时详细讲解: 加载用户的回调函数;如果能找到用户,返回用户对象;否则返回 None 。
@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))