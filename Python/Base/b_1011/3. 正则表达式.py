# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 3. 正则表达式.py
Date: 2021/10/11 14:20
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import re

s0 = '今天天气好晴朗，处处好风光呀好风光！'

# m0 = re.finditer(r'好', s0)
# print(m0)
# for i in m0:
#     print(i)


# m1 = re.fullmatch('今.*！', s0)
# print(m1)

# m2 = re.search(r'(好.*)(晴.*好)', s0)
#
# print(m2.group())  # 好晴朗，处处好风光呀好
# print(m2.group(1))  # 好
# print(m2.group(2))  # 晴朗，处处好风光呀好
#
# print(m2.pos, m2.endpos)  # 0 18
#
# print(m2.span())


# m3 = re.search(r'(?P<g1>天.*)(处.*光)', s0)
# print(m3.group('g1'))


# r = re.compile(r'好.*光')
# result = r.search(s0)
#
# print(result.group())



