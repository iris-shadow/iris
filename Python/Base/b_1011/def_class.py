# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: def_class.py
Date: 2021/10/11 13:34
Author: 吃不胖的棒棒糖(>^ω^<)
"""


class Dog(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        print(f'我叫{self.name}，性别：{self.gender}，今年{self.age}啦！')


_dog = Dog('大黄',  1, '男')

get_info = _dog.get_info

# del _dog