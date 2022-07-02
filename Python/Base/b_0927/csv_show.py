# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: csv_show.py
Date: 2021/9/23 13:41
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import csv
fw = open('example.csv', 'w', encoding='utf-8', newline='')
# 实例化一个CSV的写入对象（对普通的读对象 'fw' 进行加工）
w = csv.writer(fw)
# writerow()，写入一行数据
w.writerow(['name', 'age', 'family', 'height', 'weight'])
# writerows()，写入多行数据
w.writerows([
             ['诸葛铁锤', 11, '大宋', 11, 25],
             ['史珍香', 12, '西汉', 23, 14]
            ])
fw.close()


fr = open('example.csv', 'r', encoding='utf-8')
r = csv.reader(fr)
print(list(r))
fr.close()


