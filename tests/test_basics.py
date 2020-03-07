"""
File: test_basics.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""

import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    """

     setUp() 和 tearDown() 方法分别在各测试前后运行,并且名字以 test_ 开头的函数都作为测试执
     行。

     """

    def setUp(self):
        """
    在测试前创建一个测试环境。
           1). 使用测试配置创建程序
           2). 激活上下文, 确保能在测试中使用 current_app
           3). 创建一个全新的数据库,以备不时之需。
       :return:
       """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()  # Binds the app context to the current context.
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # Pops the app context
        self.app_context.pop()

    def test_app_exists(self):
        """
       测试当前app是否存在?
       """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
       测试当前app是否为测试环境?
       """
        #  app = create_app()
        # current_app
        self.assertTrue(current_app.config['TESTING'])
