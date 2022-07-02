# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 创建一个能实现 range(10) 的迭代器、能生成斐波那契额数列的迭代器
File: 迭代器.py
Date: 2021/9/28 16:19
Author: 吃不胖的棒棒糖(>^ω^<)
"""


# class Iterator(object):
#     def __init__(self, counter):
#         self.counter = counter
#         self.base = -1
#
#     def __iter__(self):
#         # 返回对象本身
#         return self
#
#     def __next__(self):
#         self.base += 1
#         if self.base < self.counter:
#             return self.base
#         else:
#             # 抛出 StopIteration 让迭代器停止
#             raise StopIteration


# sequence = Iterator(10)

# for i in sequence:
#     print(i)  # 0 1 2 3 4 5 6 7 8 9


class Fibonacci(object):
    def __init__(self, counter):
        self.counter = counter
        self.index = -1
        self.num1 = self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.counter:
            # 使用临时变量 temp 保存 num1 的值，实现第一二个返回值为 1
            self.temp = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return self.temp
        else:
            raise StopIteration


sequence = Fibonacci(12)

for i in sequence:
    print(i)
