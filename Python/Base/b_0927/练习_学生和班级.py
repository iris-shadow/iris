# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 
File: 练习_学生和班级.py
Date: 2021/9/27 21:55
Author: 吃不胖的棒棒糖(>^ω^<)
"""


class Student(object):
    def __init__(self, num, name, age, gender, score):
        self.num = num
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return f'{self.num:<11}{self.name:<11}{self.age:<11}{self.gender:<11}{self.score:<10}'


class Class(object):
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __str__(self):
        return print(f'{"学号":<10}{"姓名":<10}{"年龄":<10}{"性别":<10}{"分数":<10}')

    def show(self):
        """
        显示班级学生信息
        :return: 无
        """
        print('班级学生信息：')
        self.__str__()
        for student in self.students:
            print(student)
        print('-' * 55)

    def search(self, num):
        """
        按学号查询对应学生信息
        :param num: 学号
        :return: 无
        """
        print('\n查询信息如下：\n')
        info = None
        for student in self.students:
            if student.num == num:
                info = student
                break
        if info is None:
            print('无此学生')
            print('-' * 55)
        else:
            self.__str__()
            print(info)
            print('-' * 55)

    def fail(self):
        """
        查询不及格的学生
        :return: 无
        """
        fail_students = filter(lambda s: s.score < 60, self.students)
        tem = list(fail_students)
        print('\n不及格的学生有{}个：\n'.format(len(tem)))
        self.__str__()
        for student in tem:
            print(student)
        print('-' * 55)

    def order(self):
        """
        将学生按成绩降序排序
        :return: 无
        """
        print('\n成绩降序排序：\n')
        self.__str__()
        sequence = sorted(self.students, key=lambda student: student.score, reverse=True)
        for student in sequence:
            print(student)
        print('-' * 55)


s0 = Student(1, '小明', 22, '男', 100)
s1 = Student(2, '小黄', 2, '男', 16)
s2 = Student(4, '小冬', 12, '女', 20)
s3 = Student(6, '小华', 20, '男', 0)
s4 = Student(7, '小杰', 10, '男', 50)
s5 = Student(3, '小妹', 19, '女', 99)
s6 = Student(5, '小小明', 4, '女', 100)

students_list = [s0, s1, s2, s3, s4, s5, s6]
c = Class('男德三中', students_list)
c.show()
c.search(21)
c.search(1)
c.fail()
c.order()
