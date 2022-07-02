# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 练习_圆和点.py
Date: 2021/9/27 16:47
Author: 吃不胖的棒棒糖(>^ω^<)
"""
import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp, radius):
        """
        :param cp: 圆心
        :param radius: 半径
        """
        self.cp = cp
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

    def length(self):
        return math.pi * self.radius ** 2

    def relationship(self, point):
        """
        :param point: 给定与圆所处关系的点
        :return: 给定点与圆心构成直角三角形的两直角边的平方和与半径平方的比较结果
        """
        distance = (point.x - self.cp.x) ** 2 + (point.y - self.cp.y) ** 2
        if distance > self.radius ** 2:
            result = '在圆外'
        elif distance < self.radius ** 2:
            result = '在圆内'
        else:
            result = '在圆上'
        return result


# 实例化一个圆心
cp = Pointer(0, 0.0000000001)
# 实例化一个给定点
p0 = Pointer(3, 4)
# 实例化一个圆
c = Circle(cp, 5)

print(c.length())
print(c.area())
# 与理论数学有差距，涉及到不可避免的精度问题
print(c.relationship(p0))
