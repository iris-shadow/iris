# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: students_manager.py
Date: 2021/10/10 08:31
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import files_manager
import model
import students_operate
import tools

s_header = ('id', 'name', 'age', 'gender')


def select(func_name, scope):
    operate = input('请选择要进行的操作：')
    if operate in scope[:-1]:
        func_name(operate)
        content = files_manager.read_file('ask.txt')
        while True:
            print(content)
            operate0 = input('请选择要进行的操作：')
            if operate0 == '1':
                break
            elif operate0 == '2':
                return True
            else:
                print('输入不合法，请重新输入！')
    elif operate == scope[-1]:
        return True
    else:
        print('输入不合法，请重新输入！')
        return


def process(func_name, file_name, scope):
    # 判断是否有学生
    if tools.judge():
        print('您还没有学生，请添加学生！')
        return
    # 显示操作界面
    content = files_manager.read_file(file_name)
    while True:
        print(content)
        ans = select(func_name, scope)
        if ans:
            return


def add():
    content = files_manager.read_dict('students.csv', s_header)
    students = content[1:]
    while True:
        name = input('请输入姓名：')
        age = input('请输入年龄：')
        gender = input('请输入性别：')
        student = model.Students(name, age, gender)
        students.append(student.__dict__)
        print(files_manager.read_file('ask.txt'))
        while True:
            operate = input('请选择要进行的操作：')
            if operate == '1':
                break
            elif operate == '2':
                files_manager.write_dict(students, 'students.csv', s_header)
                print(('-' * 25 + '添加成功！' + '-' * 25))
                return
            else:
                print('输入不合法，请重新输入！')


def modify():
    # # 判断是否有学生
    # if tools.judge():
    #     print('您还没有学生，请添加学生！')
    #     return
    # # 显示修改界面
    # content = files_manager.read_file('modify.txt')
    # while True:
    #     print(content)
    #     operate = input('请选择要进行的操作：')
    #     if operate == '1' or operate == '2':
    #         students_operate.modify_manner(operate)
    #         content0 = files_manager.read_file('ask.txt')
    #         while True:
    #             print(content0)
    #             operate0 = input('请选择要进行的操作：')
    #             if operate0 == '1':
    #                 break
    #             elif operate0 == '2':
    #                 return
    #             else:
    #                 print('输入不合法，请重新输入！')
    #     elif operate == '3':
    #         break
    #     else:
    #         print('输入不合法，请重新输入！')
    process(students_operate.modify_manner, 'modify.txt', ('1', '2', '3'))


def search():
    # # 判断是否有学生
    # if tools.judge():
    #     print('您还没有学生，请添加学生！')
    #     return
    # # 显示查询界面
    # content = files_manager.read_file('search.txt')
    # while True:
    #     print(content)
    #     operate = input('请选择要进行的操作：')
    #     if operate == '1' or operate == '2' or operate == '3':
    #         students_operate.search_manner(operate)
    #         content0 = files_manager.read_file('ask.txt')
    #         while True:
    #             print(content0)
    #             operate0 = input('请选择要进行的操作：')
    #             if operate0 == '1':
    #                 break
    #             elif operate0 == '2':
    #                 return
    #             else:
    #                 print('输入不合法，请重新输入！')
    #     elif operate == '4':
    #         break
    #     else:
    #         print('输入不合法，请重新输入！')
    process(students_operate.search_manner, 'search.txt', ('1', '2', '3', '4'))


def delete():
    # # 判断是否有学生
    # if tools.judge():
    #     print('您还没有学生，请添加学生！')
    #     return
    # # 显示删除界面
    # content = files_manager.read_file('delete.txt')
    # while True:
    #     print(content)
    #     operate = input('请选择要进行的操作：')
    #     if operate == '1' or operate == '2':
    #         students_operate.delete_manner(operate)
    #         content0 = files_manager.read_file('ask.txt')
    #         while True:
    #             print(content0)
    #             operate0 = input('请选择要进行的操作：')
    #             if operate0 == '1':
    #                 break
    #             elif operate0 == '2':
    #                 return
    #             else:
    #                 print('输入不合法，请重新输入！')
    #     elif operate == '3':
    #         break
    #     else:
    #         print('输入不合法，请重新输入！')
    process(students_operate.delete_manner, 'delete.txt', ('1', '2', '3'))


def students_show(name):
    while True:
        content = files_manager.read_file('manager.txt') % name
        print(content)
        operate = input('请选择要进行的操作：')
        if operate == '1':
            add()
        elif operate == '2':
            modify()
        elif operate == '3':
            search()
        elif operate == '4':
            delete()
        elif operate == '5':
            break
        else:
            print('输入不合法，请重新输入！')
