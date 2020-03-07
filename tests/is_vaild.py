"""
File: is_vaild.py
Author: lvah
Date: 2020-03-07 
Connect: 976131979@qq.com
Description: 

"""


def is_age_vaild(age):
    if isinstance(age, int):
        if 0 < age < 100:
            return True
        else:
            return  False
    else:
        return  False
if __name__ == '__main__':
    assert is_age_vaild(10) == True
    assert  is_age_vaild('hello') == True