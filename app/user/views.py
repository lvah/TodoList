"""
File: views.py
Author: lvah
Date: 2020-03-12 
Connect: 976131979@qq.com
Description: 

"""
from app.models import User
from app.user import user
from flask import abort, render_template
from flask_login import  login_required

@user.route('/user/<id>')
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort(404)      # 抛出一个404异常
    else:
        return render_template('user/user.html', user=user)


@user.route('/changepwd/<id>')
def change_password(id):
    return 'change password'
