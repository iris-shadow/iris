# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 01. udp_recv.py
Date: 2021/10/12 17:53
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import socket

# 实例化一个用户数据报协议对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 指定接收数据的 ip (本机ip)和端口号
r_addr = '10.2.85.132', 1025
# 绑定 ip 和端口号（注意 bind() 内的参数是一个元组）
s.bind(r_addr)

# 指定每次接收数据大小
content = s.recvfrom(1024)

# 返回的内容是一个含有两个元素的元组，第一个是数据，第二个含有 ip 和端口号的元组
print(content)  # (b'hello', ('10.2.243.218', 8080))
# 输出数据时要进行解码
print(content[0].decode())

# 关闭对象
s.close()