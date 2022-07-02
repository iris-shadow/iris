# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: test.py
Date: 2021/9/28 17:00
Author: 吃不胖的棒棒糖(>^ω^<)
"""


def div(a, b):
    try:
        ans = a / b
    except ZeroDivisionError:
        print('错误！你个垃圾！！')
    else:
        return ans
    finally:
        # 情况 1
        print('来打我呀！略略~~~~~')
        # 情况 2
        # return '来打我呀！略略~~~~~'


print(div(1, 0))  # 情况 1 ：错误！你个垃圾！！来打我呀！略略~~~~~None | 情况 2 ：错误！你个垃圾！！来打我呀！略略~~~~~
# 情况 1 说明：else 中返回的 ans 在没有被赋值前被引用（除数为0），所以其值为空数据 None
# 情况 2 说明：函数有多个 return 返回值时，最后的返回值会覆盖前面的返回值
