# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
    @Use: 测试
    @File: 04. 多进程.py
    @Date: 2021/10/15 16:48
    @Author: ❦吃不胖的棒棒糖❄︎
"""

import multiprocessing
import random
import time


def demo(queue, name, msg):
    # 获取开始执行的时间戳
    t_start = time.time()
    # random() 产生（0, 1）的随机浮点数
    t_sleep = random.random()
    # 休眠随机参数的秒数
    time.sleep(t_sleep)
    # 获取执行结束的时间戳
    t_stop = time.time()
    # 计算耗时
    t_inter = t_stop - t_start
    other = queue.get()
    queue.put(name)
    return '{}对{}说：{}\t耗时{}秒\n'.format(other, name, msg, t_inter)


def clown1(queue, name, msg):
    return demo(queue, name, msg)


def clown2(queue, name, msg):
    return demo(queue, name, msg)


def clown3(queue, name, msg):
    return demo(queue, name, msg)


def clown4(queue, name, msg):
    return demo(queue, name, msg)


# 用于接收进程的执行结果
result = []

if __name__ == '__main__':
    # 实例化进程池对象
    p = multiprocessing.Pool(2)

    # 实例化队列对象（注意不能使用 multiprocessing.Queue() 创建，否则会报错）
    q = multiprocessing.Manager().Queue(1)
    # 放入一个元素到队列
    q.put('狗蛋')

    # 将任务分配给进程池中空闲的进程
    ret0 = p.apply_async(clown1, (q, '懒鬼', '饭否？'))
    print(ret0.get())  # 直接获取会将进程变为串行方式执行，因为 get 方法是阻塞方法
    ret1 = p.apply_async(clown2, (q, '二哈', '嗯'))
    print(ret1.get())
    ret2 = p.apply_async(clown3, (q, '狗蛋', '吃啥？'))
    print(ret2.get())
    ret3 = p.apply_async(clown4, (q, '妞妞', '饭'))
    print(ret3.get())

    p.close()
    # 此处不再需要 join 方法，因为 get 本身就是阻塞

    # 可使用异步获取执行结果方法解决
    '''
    ret0 = p.apply_async(clown1, (q, '懒鬼', '饭否？'))
    result.append(ret0)
    ret1 = p.apply_async(clown2, (q, '二哈', '嗯'))
    result.append(ret1)
    ret2 = p.apply_async(clown3, (q, '狗蛋', '吃啥？'))
    result.append(ret2)
    ret3 = p.apply_async(clown4, (q, '妞妞', '饭'))
    result.append(ret3)
    
    for i in result:
        print(i.get())
    p.close()
    p.join()
    '''
