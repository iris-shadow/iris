# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 返回客户端需要下载的文件
File: 04. tcp_file_server.py
Date: 2021/10/14 10:15
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import socket


# 定义读取文件函数（为了通用性，使用二进制读取模式）
def read(file_name):
    # if os.path.isfile(file_name):
        try:
            with open(file_name, 'rb') as f:
                content = f.read()
        except FileNotFoundError:
            content = ''
        return content
# 实例化传输控制协议对象（流式套接字）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 指定 ip（本机） 和端口号
r_addr = '10.2.243.227', 1025
# 绑定 ip 和端口号
s.bind(r_addr)

# 启用 listen 方法，使主动套接字变为被动
s.listen()

# 不断等待客户端的请求
while True:
    # 接收客户端，返回一个用于标记新客户端的套接字和新客户端的信息（ip，端口）
    client, s_addr = s.accept()
    # 接收客户端发来的数据
    file_name = client.recv(1024).decode()
    # 调用 read 函数获取客户端要下载的文件
    data = read(file_name)
    # 当客户端访问的文件存在时发送该文件
    if data:
        client.send(data)
        print('发送完毕！')
    else:
        print(file_name, '文件不存在！')
    # 关闭为该客户端服务的套接字
    client.close()

