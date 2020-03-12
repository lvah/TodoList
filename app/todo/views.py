"""
File: views.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""

# 2). 应用蓝图
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user

from app import db
from app.models import Todo
from app.todo import todo
from app.todo.forms import AddTodoForm, EditTodoForm


# 查看任务
@todo.route('/list/')
@login_required
def list():
    page = int(request.args.get('page', 1))
    # 任务显示需要分页,每个用户只能查看自己的任务
    todoPageObj = Todo.query.filter_by(
        user_id=current_user.id).paginate(
        # 在config.py文件中有设置;
        page, per_page=current_app.config['PER_PAGE'])
    return render_template('todo/list.html', todoObj=todoPageObj)


@todo.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    form = AddTodoForm()
    if form.validate_on_submit():
        # 获取用户提交的内容
        content = form.content.data
        category_id = form.category.data  # Flask学习-1
        # 添加到数据库中
        todo = Todo(content=content,
                    category_id=category_id,
                    user_id=current_user.id

                    )
        db.session.add(todo)
        flash('添加任务成功', category='success')
        return redirect(url_for('todo.add'))
    return render_template('todo/add.html', form=form)


# 编辑任务
@todo.route('/edit/<int:id>/', methods=['GET', 'POST'])
def edit(id):
    form = EditTodoForm()
    # *****重要: 编辑时需要获取原先任务的信息, 并显示到表单里面;
    todo = Todo.query.filter_by(id=id).first()
    form.content.data = todo.content
    form.category.data = todo.category_id
    if form.validate_on_submit():
        # 更新时获取表单数据一定要使用request.form方法获取,
        # 而form.content.data并不能获取用户更新后提交的表单内容;
        content = request.form.get('content')
        category_id = request.form.get('category')
        # 更新到数据库里面
        todo.content = content
        todo.category_id = category_id
        db.session.add(todo)
        flash('任务已更新', category='success')
        return redirect(url_for('todo.list'))
    return render_template('todo/edit.html', form=form)


# 删除任务: 根据任务id删除
@todo.route('/delete/<int:id>/')
@login_required
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    flash("删除任务成功", category='success')
    return redirect(url_for('todo.list'))


# 修改任务状态为完成
@todo.route('/done/<int:id>/')
@login_required
def done(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.status = True
    db.session.add(todo)
    flash('修改状态成功', category='success')
    return redirect(url_for('todo.list'))


# 修改任务状态为未完成
@todo.route('/undo/<int:id>')
@login_required
def undo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.status = False
    db.session.add(todo)
    flash("修改状态成功", category='success')
    return redirect(url_for('todo.list'))
