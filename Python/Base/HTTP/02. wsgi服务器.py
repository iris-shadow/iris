# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
    @Use: 测试
    @File: 02. wsgi服务器.py
    @Date: 2021/10/16 21:01
    @Author: ❦吃不胖的棒棒糖❄︎
"""
from wsgiref import simple_server


def index():
    return '欢迎来到网站首页！'


def register():
    return '欢迎来到注册页面！'


def login():
    return '欢迎来到登录界面！'


urls = {'/index': index, '/register': register, '/login': login}


def process(environ, start_response):
    status_code = '200 OK'
    path = environ['PATH_INFO']
    func = urls.get(path)
    if func:
        response_body = func()
    else:
        response_body = '您访问的页面浪迹天涯了！'
    start_response(status_code, [('Content-Type', 'text/plain; charset=utf-8')])
    return [response_body.encode('utf-8')]


httpd = simple_server.make_server('', 8080, process)
sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
httpd.serve_forever()