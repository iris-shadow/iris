# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 4. 规则.py
Date: 2021/10/11 16:32
Author: 吃不胖的棒棒糖(>^ω^<)
"""
import re


# s0 = '1+2+3'
#
# print(re.search(r'\+', s0))


# s1 = '大洋芋，\n\t小米渣'

# print(re.search(r'\s+', s1))  # <re.Match object; span=(4, 5), match='\n'>
#
# print(re.search(r'\S', s1))


# s2 = 'sym1218bol'
#
# print(re.search(r'm[0-9]+b', s2).group())  # m1218b


# s3 = 'exatmple'
# m0 = re.search(r'a[a-b0-9t]m', s3)
#
# print(m0.group())  # atm


# 匹配数字
# num = input('请输入数字：')
#
# if re.fullmatch(r'\d+(.\d+)?', num):
#     print(float(num))
# else:
#     print('不是数字！')


# # 用正则将字符串里的数字替换为减6
# def sub(p):
#     num = int(p.group())
#     num -= 6
#     return str(num)
#
#
# s = '一15叶2秋18'
#
# result = re.sub(r'\d+', sub, s)
#
# print(result)  # 一9叶-4秋12


# s5 = 'aa1234bbb'
#
# result = re.match(r'aa(\d+?)bbb', s5)
#
# print(result.group())
# print(result.group(1))
# # print(result.group(2))


