# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
    @Use: 测试
    @File: 01. http服务器.py
    @Date: 2021/10/16 14:12
    @Author: ❦吃不胖的棒棒糖❄︎
"""

import socket

# 实例化一个传输控制协议对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 指定 ip、端口并绑定
s_address = ('127.0.0.1', 8080)
server.bind(s_address)

# 监听是否有客户端连接，套接字由主动变被动
server.listen(128)

# 创建套接字标记新连接的客户端
client, c_address = server.accept()

# 获取客户端发来的数据
data = client.recv(1024)

# 打印数据
print('收到来自{}的数据：\n{}'.format(c_address[0], data.decode()))

# 制作响应头
response_header = 'HTTP/1.1 200 OK\n'
response_header += 'content-type:text/html;charset=utf-8\n'
# 所有响应头制作完毕后要进行换行
response_header += '\n'

# 制作响应体：
response_body = '你好，世界！'
# 拼接响应头和响应体
msg = response_header + response_body

# 发送响应消息给客户端
client.send(msg.encode('utf-8'))
