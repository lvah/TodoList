"""
File: __init__.py.py
Author: lvah
Date: 2020-03-12 
Connect: 976131979@qq.com
Description: 

"""

from flask import  Blueprint
# 1). 创建蓝图
user = Blueprint('user', __name__)


# 注意： 导入包的实质是执行包里面的__init__.py文件
from . import  views