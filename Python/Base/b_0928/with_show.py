# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: with_show.py
Date: 2021/9/28 14:14
Author: 吃不胖的棒棒糖(>^ω^<)
"""


class MyWith(object):
    def __enter__(self):
        print('我是 __enter__ 魔术方法')
        return '我是 __enter__ 的返回结果'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('我是 __exit__ 魔术方法')


with MyWith() as f:
    # f 是 MyWith() 对象调用 __enter__ 方法后返回的结果 f = MyWith().__enter__()
    print(f)  # 我是 __enter__ 的返回结果
    print(f == MyWith().__enter__())  # True

