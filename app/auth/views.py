"""
File: views.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""
# 2). 应用蓝图，管理路由
from app import db
from app.auth import auth
from app.auth.forms import RegisterationForm
from flask import render_template, flash, redirect, url_for

from app.models import User, Role


@auth.route('/')
def index():
    return  'Index'

# 报错解决： Method Not Allowed
@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    /register:
        - GET: 获取注册页面
        - POST：获取注册页面提交的数据信息
            1). 判断是否为POST方法提交数据, 并且数据是否通过表单验证.
            2). 如果通过验证， 将表单提交的数据存储到数据库中,注册成功，跳转到登录页面.

            获取表单提交的数据， 有两种方式:
                *). form.data   {'email': 'hello@qq.com', 'username': 'hello'}
                *). form.email.data, form.username.data


    :return:
    """
    form = RegisterationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.password = form.password.data
        user.email = form.email.data
        user.role = Role.query.filter_by(name="普通会员").first()
        db.session.add(user)
        flash("用户%s注册成功" %(user.username))
        # return  redirect('/login')
        # url_for('auth.login')根据视图函数寻找对应的路由地址， /login
        return  redirect(url_for('auth.login'))
    return  render_template('auth/register.html', form=form)


@auth.route('/login')
def login():
    return  'login'


@auth.route('/logout')
def logout():
    return  'logout'