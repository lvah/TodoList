"""
File: views.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""

# 2). 应用蓝图
from app.todo import todo

# /todo/add/
@todo.route('/add/')
def add():
    return  'todo add'

# /todo/delete
@todo.route('/delete/')
def delete():
    return  'todo delete'