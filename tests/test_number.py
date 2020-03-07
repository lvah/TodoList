"""
File: test_number.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""
import unittest
import random

class TestSequenceFunctions(unittest.TestCase):
    """
     setUp() 和 tearDown() 方法分别在各测试前后运行,并且名字以 test_ 开头的函数都作为测试执行。
    """
    def setUp(self) -> None:
        self.seq = [0, 1, 2, 3, 4, 5, 6, 7]

    def test_choice_ok(self):
        """
        测试choice方法
        """
        item = random.choice(self.seq)
        result = item in self.seq
        self.assertTrue(result)

    def test_sample_ok(self):
        """
        测试sample方法
        """
        result = random.sample(self.seq, 4)
        self.assertEqual(len(result), 4)

    def tearDown(self) -> None:
        del self.seq



