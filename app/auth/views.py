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
from flask import render_template, flash, redirect, url_for, session, request

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
        # 接收人用列表存储
        send_mail(to=[user.email, ], subject="请激活你的任务管理平台帐号",
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
            return redirect(url_for('todo.index'))
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


# http://127.0.0.1:5000/confirm/chdchjefjhreufhrufrfhyre
# /confirm/chdchjefjhreufhrufrfhyry
# /confirm/chdchjefjhreufhrufrfhyrz
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    """
    1. 判断账户是否验证， 如果已经验证， 跳转到主页
    2. 如果没有验证， 执行验证函数，更新账户的confirmed值。
    """
    if current_user.confirmed:
        return redirect(url_for('todo.index'))
    if current_user.confirm(token):
        flash('验证邮箱通过', category='success')
    else:
        flash('验证连接失效', category='error')
    return redirect(url_for('todo.index'))


@auth.before_app_request
def before_request():
    """
    钩子函数， 当用户登录且未邮箱确认账户那么进入unconfirmed的页面。
    request.endpoint: /login ==='auth.login'
    auth中的login，register，logout.....或者static的静态文件， 都不会拦截
    :return:
    """
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    # 如果当前用户是匿名用户或者已经验证的用户, 则访问主页, 否则进入未验证界面;
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('todo.index'))
    token = current_user.generate_confirmation_token()
    return render_template('auth/unconfirmed.html')


@auth.route('/reconfirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    try:
        send_mail([current_user.email], '请激活你的任务管理平台帐号',
                  'auth/confirm', user=current_user, token=token)
    except Exception as e:
        print(e)
        flash(str(e), category='error')
        return redirect(url_for('auth.register'))
    else:
        flash('新的平台验证消息已经发送到你的邮箱, 请确认后登录.', category='success')
        return redirect(url_for('todo.index'))
