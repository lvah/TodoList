"""
File: views.py
Author: lvah
Date: 2020-03-12 
Connect: 976131979@qq.com
Description: 

"""
from app import db
from app.models import User
from app.user import user
from flask import abort, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from app.user.forms import EditProfileForm


@user.route('/user/<id>')
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort(404)  # 抛出一个404异常
    else:
        return render_template('user/user.html', user=user)


@user.route('/changepwd/<id>')
def change_password(id):
    return 'change password'


@user.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('用户配置信息更新成功!', category='success')
        return redirect(url_for('user.get_user', id=current_user.id))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('user/edit_profile.html', form=form)
