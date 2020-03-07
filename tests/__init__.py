"""
File: __init__.py.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description:

测试从软件开发过程可以分为：


    与程序开发人员最密切的就是单元测试，
    因为单元测试是由开发人员进行的，而其他测试都由专业的测试人员来完成。所以我们主要学习单元测试。

常用的断言方法：
    assert a==b
    assert a != b
    assert a== True
    assert b is False

    assertEqual     如果两个值相等，则pass
    assertNotEqual  如果两个值不相等，则pass
    assertTrue      判断bool值为True，则pass
    assertFalse     判断bool值为False，则pass
    assertIsNone    不存在，则pass
    assertIsNotNone 存在，则pass

verbosity,表示测试结果的信息复杂度，有0、1、2 三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息


"""
