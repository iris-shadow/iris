# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: index.py
Date: 2021/10/8 22:18
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import files_manager
import model
import tools
import students_manager

t_header = ('name', 'password')


def login():
    while True:
        content = files_manager.read_dict('teachers.csv', t_header)
        name = input('请输入姓名:')
        for i in content[1:]:
            if name == i.get('name'):
                password = input('请输入密码：')
                if tools.encrypt(password) == i.get('password'):
                    students_manager.students_show(name)
                    return
                else:
                    print('密码错误，请重新输入！')
                    break
        else:
            print('用户不存在，请注册！')
            return


def register():
    # 读取 teachers.csv 中的内容
    content = files_manager.read_dict('teachers.csv', t_header)
    teachers = content[1:]
    # 若读取数据除表头外还有其他内容，将除表头外的内容加到 teacher = []
    while True:
        # 用户存在标志
        exist = False
        name = input('请输入姓名（2 ～ 5位）：')
        # 判断用户是否已被注册
        for i in content:
            if name == i.get('name'):
                exist = True
                print('用户已存在，请重新输入！')
                break
        # 用户存在时，继续下一次 while 循环
        if exist:
            continue
        if not 2 <= len(name) <= 5:
            print('姓名不合法，请重新输入！')
        else:
            break
    while True:
        password = input('请输入密码（6 ～ 11位，包含数字和字母）：')
        if password.isalpha() or password.isdigit() or not 6 <= len(password) <= 11:
            print('密码不合法，请重新输入！')
        else:
            # 使用 model 模块中的 Teacher 实例化一个 teacher
            teacher = model.Teacher(name, tools.encrypt(password))
            break
    # 将 teacher 属性以字典形式保存到 teachers
    teachers.append(teacher.__dict__)
    files_manager.write_dict(teachers, 'teachers.csv', t_header)
    print('-' * 25 + '注册成功！' + '-' * 25)


def start():
    # 读取主界面
    content = files_manager.read_file('welcome.txt')
    # 选择功能
    while True:
        print(content)
        operate = input('请选择要进行的操作：')
        if operate == '1':
            login()
        elif operate == '2':
            register()
        elif operate == '3':
            break
        else:
            print('输入不合法，请重新输入！')


start()
