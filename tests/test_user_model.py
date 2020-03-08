"""


"""

import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):
    """
   用户数据库模型测试
   """
    def test_password_setter(self):
        """测试新建的用户密码是否为空?"""
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        """测试获取密码信息是否报错?"""
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            password = u.password

    def test_password_verification(self):
        """测试加密密码和明文密码是否验证正确?"""
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        """测试每次密码加密的加密字符是否不一致?"""
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
