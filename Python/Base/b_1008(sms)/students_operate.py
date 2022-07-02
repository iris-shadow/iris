# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: students_operate.py
Date: 2021/10/10 11:30
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import files_manager
import tools


def modify_manner(way):
    content = files_manager.read_dict('students.csv', tools.s_header)
    key = value = ''
    students = tools.find(way)
    if tools.show(students):
        return
    choice = int(input('请输入要修改的学生序号：'))
    while len(students) < choice:
        print('输入不合法，请重新输入！')
        choice = int(input('请输入要修改的学生序号：'))
    while True:
        operate = input(files_manager.read_file('modify_ask.txt') + '\n请选择要修改的属性：')
        if operate == '1':
            key = 'name'
            value = input('请输入新的姓名：')
            break
        elif operate == '2':
            key = 'age'
            value = input('请输入新的年龄：')
            break
        elif operate == '3':
            key = 'gender'
            value = input('请输入新的性别：')
            break
        elif operate == '4':
            return
        else:
            print('输入不合法，请重新输入！')
    index = content.index(students[choice - 1])
    content[index][key] = value
    files_manager.write_dict(content[1:], 'students.csv', tools.s_header)
    print('-' * 25 + '修改成功！' + '-' * 25)


def search_manner(way):
    students = tools.find(way)
    tools.show(students)


def delete_manner(way):
    content = files_manager.read_dict('students.csv', tools.s_header)
    students = tools.find(way)
    if tools.show(students):
        return
    choice = int(input('请输入要删除的学生序号：'))
    while len(students) < choice:
        print('输入不合法，请重新输入！')
        choice = int(input('请输入要删除的学生序号：'))
    content.remove(students[choice - 1])
    files_manager.write_dict(content[1:], 'students.csv', tools.s_header)
    print('-' * 25 + '删除成功！' + '-' * 25)
