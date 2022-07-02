# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 03. 多线程聊天.py
Date: 2021/10/14 18:09
Author: 吃不胖的棒棒糖(>^ω^<)
"""
import socket
import threading

# 指定 ip 和端口号
s_addr = ('10.2.244.6', 8080)
# 创建传输控制协议对象（服务器）
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定 ip 和客户端
server.bind(s_addr)


# 定义 server_socket 函数不断监听是否有客户端连接
def server_socket():
    # 格式化输出（服务器名提示）
    print(threading.current_thread().name.ljust(49), end='')
    while True:
        # 监听是否有新用户连接
        server.listen()
        # 创建一个用于标记新用户的套接字
        client, s_addr = server.accept()
        # 获取客户端发的信息
        msg = client.recv(1024).decode()
        print('收：'.rjust(50), msg)
        # 发送信息给客户端
        msg = input('发：'.rjust(50)).encode()
        if msg == '':
            break
        client.send(msg)
        # 关闭该客户端
        # client.close()


# 定义client_socket 函数不断向客户端请求连接
def client_socket():
    # 格式化输出（客户端名提示）
    print(threading.current_thread().name)
    while True:
        # 创建一个传输控制协议对象（客户端）
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务器
        client.connect(s_addr)
        msg = input('发：').encode()
        if msg == '':
            server.close()
            client.close()
            break
        client.send(msg)
        # 发送信息给服务器
        msg = client.recv(1024).decode()
        print('收：', msg)
        client.close()


t1 = threading.Thread(target=server_socket, name='妞妞')
t2 = threading.Thread(target=client_socket, name='可豆')

t1.start()
t2.start()
