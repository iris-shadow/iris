# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 将python数据写入到文件的方法：1. 字符串 --> json 2. 二进制 --> pickle
File: json_show.py
Date: 2021/9/25 16:40
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import json

# d0 = {'name': '诸葛铁锤', 'age': 12, 'height': 1.3}
# # 将 python 数据类型转换为 json 对应数据类型
# content = json.dumps(d0)
# file = open('test.txt', 'w', encoding='utf-8')
# file.write(content)  # test.txt: {"name": "\u8bf8\u845b\u94c1\u9524", "age": 12, "height": 1.3}
# file.close()

# file = open('test.txt', 'r', encoding='utf-8')
# content = file.read()
# print(json.loads(content))  # {'name': '史珍香', 'age': 102, 'height': 18}
# file.close()


# d1 = {'name': '史珍香', 'age': 102, 'height': 18}
# file = open('test.txt', 'w', encoding='utf-8')
# # 将 python 数据转换为 json 对应的数据类型，并将其写入到对应文件中
# json.dump(d1, file)  # test.txt： {"name": "\u53f2\u73cd\u9999", "age": 102, "height": 18}
# file.close()

file = open('test.txt', 'r', encoding='utf-8')
content = json.load(file)
print(content)  # {'name': '史珍香', 'age': 102, 'height': 18}
