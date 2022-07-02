# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
Use: 练习 Dog、Cat 子类与 Pet 父类之间的继承，强化字符串格式化输出和 __str__ 的使用
File: 练习_宠物.py
Date: 2021/9/27 19:49
Author: 吃不胖的棒棒糖(>^ω^<)
"""


class PetShop(object):
    def __init__(self, name, pets=None):
        self.name = name
        if pets is None:
            pets = []
            return
        self.pets = pets

    @staticmethod
    def show():
        print(f'\n本店共有宠物{len(pet_list)}个，如下：\n')
        print(f'{"姓名":<10}{"年龄":<10}{"性别":<10}{"种类":<10}{"颜色":<10}{"眼色":<10}')
        for pet in pet_list:
            print(pet)


class Pet(object):
    def __init__(self, name, age, gender, kind, color):
        self.name = name
        self.age = age
        self.gender = gender
        self.kind = kind
        self.color = color

    def call(self):
        print(self.name + '正在吼叫 。。。。。。')

    def eat(self):
        print(self.name + '正在吃饭 。。。。。。')

    def __str__(self):
        return f'{self.name:<10}{self.age:<12}{self.gender:<10}{self.kind:<10}{self.color:<10}{"--":<10}'


class Dog(Pet):
    def call(self):
        print(self.name + '正在汪汪汪 。。。。。。')


class Cat(Pet):
    def __init__(self, name, age, gender, kind, color, eye_color):
        super(Cat, self).__init__(name, age, gender, kind, color)
        self.eye_color = eye_color

    def call(self):
        print(self.name + '正在喵喵喵 。。。。。。')

    def __str__(self):
        return f'{self.name:<10}{self.age:<12}{self.gender:<10}{self.kind:<10}{self.color:<10}{self.eye_color:<10}'


dog0 = Dog('大黄', 1, '男', '白色', '拉布拉多')
dog1 = Dog('二妞', 1.3, '女', '黄色', '藏獒')
cat0 = Cat('大橘', 0.5, '女', '花色', '短英', '绿色')
cat1 = Cat('小妹', 1.2, '男', '红色', '波斯', '蓝色')

pet_list = [dog0, dog1, cat0, cat1]
pet_shop = PetShop('美眉', pet_list)

pet_shop.show()
