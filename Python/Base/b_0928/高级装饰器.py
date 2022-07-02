# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 高级装饰器.py
Date: 2021/9/28 15:35
Author: 吃不胖的棒棒糖(>^ω^<)
"""

HOLD = 15
R = 1  # 0b 0001
W = 2  # 0b 0010
E = 4  # 0b 0100
D = 8  # 0b 1000


def decorate(own, verify):
    def outer(fn):
        def inner():
            if own & verify:
                fn()
            else:
                print('对不起，您没有权限！')

        return inner

    return outer


@decorate(HOLD, R)
def read():
    print('正在玩命读取内容中------------O(∩_∩)O哈哈~')


@decorate(HOLD, W)
def write():
    print('正在玩命写入内容中------------O(∩_∩)O哈哈~')


@decorate(HOLD, E)
def execute():
    print('正在玩命执行中------------O(∩_∩)O哈哈~')


@decorate(HOLD, D)
def delete():
    print('正在玩命删除中------------O(∩_∩)O哈哈~')


# read()  # 正在玩命读取内容中------------O(∩_∩)O哈哈~
# write()  # 正在玩命写入内容中------------O(∩_∩)O哈哈~
# execute()  # 正在玩命执行中------------O(∩_∩)O哈哈~
delete()  # 正在玩命删除中------------O(∩_∩)O哈哈~
