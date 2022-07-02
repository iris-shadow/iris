# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 5. 练习.py
Date: 2021/10/12 15:45
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import re

"""
匹配用户名
要求：
1. 只能包含数字、字母、下划线
2. 不能以数字开头
3. 长度为 6 - 15 位
"""

# while True:
#     password = input('请输入用户名：')
#     if password == '':
#         break
#     else:
#         # ret = re.match(r'^[a-zA-Z_][0-9a-zA-Z]{5,15}$', password)
#         ret = re.fullmatch(r'[a-zA-Z_][0-9a-zA-Z]{5,15}', password)
#         if ret is None:
#             print('用户名不合法！')
#         else:
#             print(ret.group())


"""
匹配密码
要求：
1. 不能包含 ！@ ¥ # ^ & * 等字符
2. 必须以字母开头
3. 长度为 6 - 12 位
"""

# while True:
#     password = input('请输入密码：')
#     if password == '':
#         break
#     else:
#         ret = re.match(r'^[a-zA-Z][^!@$¥#…^&*]{5,11}$', password)
#         if ret is None:
#             print('密码不合法！')
#         else:
#             print(ret.group())


"""
匹配IP
"""

while True:
    ip = input('请输入IP：')
    if ip == '':
        break
    else:
        ret = re.fullmatch(r'(([0-9]|[1-9]\d|(1[0-9]{,2}|2[0-4]\d|25[0-5]))\.){3}([0-9]|[1-9]\d|(1[0-9]{,2}|2[0-4]\d|25[0-5]))', ip)
        if ret is None:
            print('IP不合法！')
        else:
            print(ret.group())


