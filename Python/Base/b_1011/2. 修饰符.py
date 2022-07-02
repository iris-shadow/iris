# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 2. 修饰符.py
Date: 2021/10/11 16:05
Author: 吃不胖的棒棒糖(>^ω^<)
"""
import re

s0 = '我每天往山上搬\n一块砖，于是就有了长城\nbird\ncat\napple\norange'
# m0 = re.search(r'我.*砖', s0, re.S)
#
# print(m0)  # <re.Match object; span=(0, 11), match='我每天往山上搬\n一块砖'>

s1 = 'syMbol'
# m1 = re.search(r'm', s1, re.I)
#
# print(m1)  # <re.Match object; span=(2, 3), match='M'>


result = re.findall(r'\w+$', s0, re.M)

print(result)  # ['我每天往山上搬', '于是就有了长城', 'bird', 'cat', 'apple', 'orange']
