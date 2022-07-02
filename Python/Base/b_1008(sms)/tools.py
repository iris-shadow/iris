# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: tools.py
Date: 2021/10/8 22:57
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import hashlib

import files_manager

s_header = ('id', 'name', 'age', 'gender')
# content = files_manager.read_dict('students.csv', s_header)


def encrypt(password):
    h = hashlib.sha256()
    h.update(password.encode('utf-8'))
    return h.hexdigest()


def judge():
    content = files_manager.read_dict('students.csv', s_header)
    if len(content) < 2:
        return True


def find(operate):
    content = files_manager.read_dict('students.csv', s_header)
    key = value = ''
    if operate == '1':
        key = 'id'
        value = input('请输入学号：')
    elif operate == '2':
        key = 'name'
        value = input('请输入姓名：')
    students = filter(lambda student: student.get(key, '') == value, content[1:])
    temp_students = list(students)
    if not len(temp_students):
        return '查无此人！'
    return temp_students


def show(result):
    if '查无此人' in result:
        print('*' * 56, '\n\t\t\t\t\t查询结果')
        print('\t\t\t\t\t查无此人！')
        print('*' * 56)
        return True
    print('*' * 56, '\n\t\t\t\t\t查询结果')
    print(f'\t\t{"序号":^5}{"id":^5}{"姓名":^5}{"年龄":^5}{"性别":^5}')
    for index, i in enumerate(result):
        print(f'\t\t{index + 1:^5}{i.get("id"):^5}{i.get("name"):^5}{i.get("age"):^5}{i.get("gender"):^5}')
    print('*' * 56)
