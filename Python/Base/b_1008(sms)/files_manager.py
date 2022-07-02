# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: files_manager.py
Date: 2021/10/8 22:19
Author: 吃不胖的棒棒糖(>^ω^<)
"""
import csv

base_dir = './files/'


def read_file(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print('文件未找到！')


def write_file(content, file_name):
    with open(base_dir + file_name, 'w', encoding='utf-8') as f:
        f.write(content)


def write_dict(content, file_name, header):
    with open(base_dir + file_name, 'w', encoding='utf-8') as f:
        f = csv.DictWriter(f, fieldnames=header)
        f.writeheader()
        f.writerows(content)


def read_dict(file_name, header):
    try:
        with open(base_dir + file_name, 'r', encoding='utf-8') as f:
            content = csv.DictReader(f, fieldnames=header)
            return list(content)
    except FileNotFoundError:
        print('文件未找到！')


