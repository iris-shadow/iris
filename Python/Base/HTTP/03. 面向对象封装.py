# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
    @Use: 测试
    @File: 03. 面向对象封装.py
    @Date: 2021/10/16 17:09
    @Author: ❦吃不胖的棒棒糖❄︎
"""
import socket


# 定义一个服务器类
class Server(object):
    # 需要 ip、端口号等属性
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen(128)

    # 静态方法，用于读取客户端访问的资源
    @staticmethod
    def read(path):
        try:
            # 注意文件的路径
            with open('.' + path, 'rb') as f:
                data = f.read()
        except Exception:
            data = '呜呜～ 您访问的文件浪迹天涯啦！'.encode('utf-8')
        return data

    # 处理客户的请求
    def process(self):
        # 创建套接字标记新连接的客户端
        client, address = self.socket.accept()

        # 接收客户端发送的数据
        request_header = client.recv(1024).decode()

        # 默认请求的文件名为空
        path = ''
        # 检测客户端发送是否有发送请求头
        if request_header:
            # 利用字符串相关操作获取客户端请求的资源
            path = request_header.splitlines()[0].split(' ')[1]
            print('{}请求了资源：{}'.format(str(address), path))
        # 调用 read 方法读取请求的资源
        response_body = self.read(path)

        # 制作响应头
        response_header = 'HTTP/1.1 200 OK\n'
        # 若请求资源不存在则改写响应头（状态码）
        if response_body == '呜呜～ 您访问的文件浪迹天涯啦！'.encode('utf-8'):
            response_header = 'HTTP/1.1 404 NOT FOUND\n'
        response_header += 'content-type:text/html;charset=utf-8\n'
        # 所有响应头制作完毕后要进行换行
        response_header += '\n'

        # 拼接响应头和响应体
        info = response_header.encode('utf-8') + response_body

        # 发送响应头和响应体给客户端
        client.send(info)

        # 关闭客户端
        client.close()


server = Server('0.0.0.0', 8080)

while True:
    server.process()
