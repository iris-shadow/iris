# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
    @Use: 测试
    @File: 04. 装饰器管理请求路径.py
    @Date: 2021/10/16 14:47
    @Author: ❦吃不胖的棒棒糖❄︎
"""

from wsgiref import simple_server

# 定义正常状态码（全局变量，方便统一管理）
normal_status = '200 OK'
# 定义的异常状态码（全局变量）
abnormal_status = '404 NOT FOUND'

# 定义一个字典保存路径（key 是请求路径，value 是处理请求路径的函数）
urls = {}


# 定义一个高级装饰器用于对请求路径和处理相关路径函数的匹配
def route(url):
    def decorator(func):
        urls[url] = func

        def inner(start_response):
            return func(start_response)

        return inner

    return decorator


# 首页处理函数 当请求路径为 '/' 或 '/index' 时都调用此函数
@route('/')
@route('/index')
def index(start_response):
    # 处理相关路径的函数可以把发送响应头的函数 start_response 拿过来，以方便修改添加等
    start_response(normal_status, [('Content-Type', 'text/html;charset=utf-8')])
    # 此处创建响应体（功能复杂时也可将其定义在其它模块然后导入调用）
    response_body = '欢迎来到网站首页！'
    # 返回响应体
    return response_body


@route('/register')
def register(start_response):
    start_response(normal_status, [('Content-Type', 'text/html;charset=utf-8')])
    response_body = '欢迎来到注册页面！'
    return response_body


@route('/login')
def login(start_response):
    start_response(normal_status, [('Content-Type', 'text/html;charset=utf-8')])
    response_body = '欢迎来到登录页面！'
    return response_body


def process(environ, start_response):
    # environ 是一个含有全部 http 请求信息的字典，使用 'PATH_INFO' 获取请求路径
    path = environ.get('PATH_INFO')
    # 从 urls 字典中获取对应路径的处理函数
    func = urls.get(path)
    # 检测请求路径是否存在
    if func:
        response_body = func(start_response)
    else:
        # 请求路径不存在时修改响应头的状态码
        start_response(abnormal_status, [('Content-Type', 'text/html;charset=utf-8')])
        response_body = '呜呜～ 您访问的页面浪迹天涯啦～'
    return [response_body.encode('utf-8')]


# 创建 wsgi 实例，需要ip（默认为 '0.0.0.0'）、端口、处理请求和响应的函数
httpd = simple_server.make_server('', 8080, process)
sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")

httpd.serve_forever()
