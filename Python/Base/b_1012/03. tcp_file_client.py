# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 03. tcp_file_client.py
Date: 2021/10/14 10:28
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import socket

# 实例化一个传输控制协议对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 指定连接服务器的 ip 和端口号
s_addr = '10.2.243.227', 1025

# 与服务器建立连接
s.connect(s_addr)

# 输入要下载的文件名
file_name = input('请输入你要下载的文件名：')
# 发送文件名给服务器
s.send(file_name.encode())

# 尝试读取是否收到数据
data = s.recv(1024)
# 如果收到数据
if data:
    # 将数据写到对应的文件名中
    with open(file_name, 'wb') as f:
        while True:
            f.write(data)
            data = s.recv(1024)
            if not data:
                break
        print('下载完成！')
# 为读取到数据（说明文件不存在）
else:
    print('文件不存在！')

# 关闭传输控制协议对象
s.close()
