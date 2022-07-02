# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 生成器.py
Date: 2021/9/30 12:52
Author: 吃不胖的棒棒糖(>^ω^<)
"""


def fibonacci(n):
    num1 = num2 = 1
    counter = 0
    while counter < n:
        counter += 1
        yield num1
        num1, num2 = num2, num1 + num2


g = fibonacci(12)

for i in g:
    print(i)

# class MyIterator(object):
#     def __init__(self, counter):
#         self.num1 = self.num2 = 1
#         self.index = 0
#         self.counter = counter
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < self.counter:
#             self.index += 1
#             self.temp = self.num1
#             self.num1, self.num2 = self.num2, self.num1 + self.num2
#             return self.temp
#         else:
#             raise StopIteration
#
#
# sequence = MyIterator(12)
# for i in sequence:
#     print(i)
