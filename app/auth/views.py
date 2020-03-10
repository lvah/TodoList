"""
File: views.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""
# 2). 应用蓝图，管理路由
from flask_login import login_user, logout_user, login_required

from app import db
from app.auth import auth
from app.auth.forms import RegisterationForm, LoginForm
from flask import render_template, flash, redirect, url_for, session

from app.auth.send_mail import send_mail
from app.models import User, Role
from flask_login import current_user


@auth.route('/')
def index():
    return render_template('auth/index.html')


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
        flash("用户%s注册成功" % (user.username), category='success')
        # 提交数据库之后才能赋予新用户 id 值,而确认令牌需要用到 id ,所以不能延后提交。
        token = user.generate_confirmation_token()
        print(user.email, token)
        send_mail(to=[user.email,], subject="请激活你的任务管理平台帐号",
                  filename='auth/confirm', user=user, token=token)
        flash("'平台验证消息已经发送到你的邮箱, 请确认后登录.", category='success')
        # return  redirect('/login')
        # url_for('auth.login')根据视图函数寻找对应的路由地址， /login
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 判断用户是否存在并且密码是否正确.
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash("用户%s登录成功" % (user.username), category='success')
            return redirect(url_for('auth.index'))
        else:
            flash("用户%s登录失败" % (form.email.data), category='error')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("用户注销成功", category='success')
    return redirect(url_for('auth.index'))
