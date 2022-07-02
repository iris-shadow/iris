# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: pickle_show.py
Date: 2021/9/27 14:47
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import pickle

# info = {'name': '史珍香', 'age': 102, 'height': 18}
# file = open('test.txt', 'wb')
# # 将 info 转化为二进制数据
# content = pickle.dumps(info)
# file.write(content)
# file.close()


# info = {'name': '史珍香', 'age': 102, 'height': 18}
# file = open('test.txt', 'wb')
# pickle.dump(info, file)
# file.close()


# file = open('test.txt', 'rb')
# content = file.read()
# print(pickle.loads(content))  # {'name': '史珍香', 'age': 102, 'height': 18}
# file.close()

file = open('test.txt', 'rb')
content = pickle.load(file)
print(content)  # {'name': '史珍香', 'age': 102, 'height': 18}
