# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 02. 线程通信.py
Date: 2021/10/14 14:54
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import threading
import queue
import time

q = queue.Queue()


def produce():
    for i in range(10):
        food = '大洋芋' + str(i)
        q.put(food)
        print(threading.current_thread().name + '生产了一个' + food)
        time.sleep(0.1)


def reduce():
    for j in range(10):
        food = q.get()
        print(threading.current_thread().name + '消费了一个' + food)
        time.sleep(0.2)


t1 = threading.Thread(target=produce, name='生产者')
t2 = threading.Thread(target=reduce, name='消费者')

t1.start()
t2.start()
