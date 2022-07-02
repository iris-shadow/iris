# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 1. 模块中类方法的调用.py
Date: 2021/10/11 13:33
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import def_class

def_class.get_info()

def_class.Dog.get_info(def_class.Dog('大白', 2, '女'))

def_class._dog.get_info()  # _dog为私有属性，在导入模块中可能在末尾会被删除，调用使会报错
