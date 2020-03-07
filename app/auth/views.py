"""
File: views.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""
# 2). 应用蓝图，管理路由
from app.auth import auth

@auth.route('/')
def index():
    return  'Index'


@auth.route('/register')
def register():
    return  'register'


@auth.route('/login')
def login():
    return  'login'


@auth.route('/logout')
def logout():
    return  'logout'