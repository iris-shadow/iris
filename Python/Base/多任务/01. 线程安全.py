# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 01. 线程安全.py
Date: 2021/10/14 13:48
Author: 吃不胖的棒棒糖(>^ω^<)
"""

import threading
import time

lock = threading.Lock()

ticket = 20

def sell_ticket():
    global ticket
    while True:
        lock.acquire()
        if ticket > 0:
            time.sleep(0.5)
            ticket -= 1
            lock.release()
            print('{}卖出了1张票，还剩{}张'.format(threading.current_thread().name, ticket))
        else:
            lock.release()
            print('卖完了')
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
