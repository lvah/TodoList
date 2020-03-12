"""
File: forms.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

from app.models import Category


class AddTodoForm(FlaskForm):
    content = StringField(
        label='任务内容',
        validators=[DataRequired()]

    )
    # 下拉表
    category = SelectField(
        label='任务类型',
        coerce=int,   # 存的是id整形
        # choices=[(item.id, item.name) for item in Category.query.all()]

    )
    submit = SubmitField(
        label='添加任务',

    )

    def __init__(self):
        # 执行父类的构造方法。
        super(AddTodoForm, self).__init__()
        categories = Category.query.all()
        if categories:
            self.category.choices = [(item.id, item.name) for item in
                                     categories]
        else:
            self.category.choices = [(-1, "请先创建分类")]


class EditTodoForm(FlaskForm):
    content = StringField(
        label='任务内容',
        validators=[DataRequired()]

    )
    category = SelectField(
        label='任务类型',
        coerce=int,  # 存的是id整形
        # choices=[(item.id, item.name) for item in Category.query.all()]

    )
    submit = SubmitField(
        label='编辑任务',

    )

    def __init__(self):
        super(EditTodoForm, self).__init__()
        categories = Category.query.all()
        if categories:
            self.category.choices = [(item.id, item.name) for item in
                                     categories]
        else:
            self.category.choices = [(-1, "请先创建分类")]