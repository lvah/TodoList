# 1). 创建蓝图
from flask import  Blueprint
todo = Blueprint('todo', __name__)
from . import  views