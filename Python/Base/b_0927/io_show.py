# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: io_show.py
Date: 2021/9/23 14:51
Author: 吃不胖的棒棒糖(>^ω^<)
"""

from io import StringIO, BytesIO

fs = StringIO()
fs.write('Enter the content')
# 从内存中获取数据
print(fs.getvalue())  # Enter the content
fs.close()

fb = BytesIO()
fb.write('Enter the content'.encode(encoding='utf-8'))
print(fb.getvalue())  # b'Enter the content'
fb.close()
