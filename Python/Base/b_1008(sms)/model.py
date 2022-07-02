# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: model.py
Date: 2021/10/8 22:56
Author: 吃不胖的棒棒糖(>^ω^<)
"""
import files_manager

content = files_manager.read_file('key.txt')
if content == '':
    s_id = 0
else:
    s_id = int(content)


class Teacher(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Students(object):
    def __init__(self, name, age, gender):
        self.id = s_id + 1
        self.name = name
        self.age = age
        self.gender = gender
        files_manager.write_file(str(self.id), 'key.txt')

