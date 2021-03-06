# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: test.py
Date: 2021/10/14 12:39
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import socket

# 实例化一个用户数据报协议对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 指定接收数据的 ip (本机ip)和端口号
r_addr = '192.168.0.1', 1025
s_addr = '192.168.0.5', 8080
# 绑定 ip 和端口号（注意 bind() 内的参数是一个元组）
s.bind(r_addr)
while True:
    msg = input('请输入要发送的信息：')
    s.sendto(msg.encode(), s_addr)

    # 指定每次接收数据大小
    content = s.recvfrom(1024)

    # 返回的内容是一个含有两个元素的元组，第一个是数据，第二个含有 ip 和端口号的元组
    print(content)  # (b'hello', ('10.2.243.218', 8080))
    # 输出数据时要进行解码
    print(content[0].decode())

    # 关闭对象
    # s.close()