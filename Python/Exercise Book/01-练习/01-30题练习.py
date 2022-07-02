# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
@Use: 
@File: 01-30题练习.py
@Date: 2021/11/13 12:29 下午
@Author: 🐼吃不胖的🐬棒棒糖🐹
"""

'''
# 1. 已知一个字符串为 “hello_world_yoyo”，如何得到一个队列 [“hello”,”world”,”yoyo”] ？

s0 = 'hello_world_yoyo'
split_s0 = s0.split('_')
print(split_s0)

# 2. 有个列表 [“hello”, “world”, “yoyo”]，如何把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”？

# 方法1：
l0 = ['hello', 'world', 'yoyo']
join_l0 = '_'.join(l0)
print(join_l0)

# 方法2：
join_l1 = ''
for i in l0:
    join_l1 += i + '_'
print(join_l1.rstrip('_'))

# 3. 把字符串 s 中的每个空格替换成”%20”，输入：s = “We are happy.”，输出：“We%20are%20happy.”。

s1 = 'We are happy.'
replace_s1 = s1.replace(' ', '%20')
print(replace_s1)

# 4. Python 如何打印 99 乘法表？

# 方法1（for 实现）：
for i in range(1, 10):
    for j in range(1, i + 1):
        # print(j, '*', i, '=', i * j, end='')
        # print('\t', end='')
        # 上面两个 print 语句可换为
        print('{} * {} = {}\t'.format(j, i, i * j), end='')
    print()

# 方法2（while 实现）：
i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print('%d * %d = %-4d' % (j, i, i * j), end='')
    print()


# 5. 从下标 0 开始索引，找出单词 “welcome” 在字符串“Hello, welcome to my world.” 中出现的位置，找不到返回 -1。

# 方法1：
s2 = 'Hello, welcome to my world.'
index = s2.find('welcome')
print(index)


# 方法2：
def find(d_str, o_str):
    d_len = len(d_str)
    for i in range(0, len(o_str) - d_len + 1):
        if o_str[i:i + d_len] == d_str:
            return i
    else:
        return -1


index = find('welcome', s2)
print(index)


# 6. 统计字符串“Hello, welcome to my world.” 中字母 w 出现的次数。

# 方法1：
s3 = 'Hello, welcome to my world.'
count = 0
for i in s3:
    if i == 'w':
        count += 1
print(count)

# 方法2：
count = s3.count('w')
print(count)


# 7. 输入一个字符串 str，输出第 m 个只出现过 n 次的字符，如在字符串 gbgkkdehh 中，找出第 2 个只出现 1 次的字符，输出结果：d

def search():
    string = input('请输入字符串：')
    index = int(input('请输入查找位次：'))
    count = int(input('请输入出现个数：'))
    # 准备一个字典以 字符出现次数:[字符1下标, 字符2下标, ...] 的形式存储（以键来查询出现的次数，值的下标查询第几次，值的数据查询该字符在字符串中的下标）
    times = {}
    # 使用字典去重，根据字符串中字符的个数来确定需要建立多少个键值对
    tem_string = set(string)
    # 建立键值对
    for key in range(len(tem_string)):
        times[key] = []
    # 遍历字符串，将每个字符出现的次数及其下标以键值对方式存储
    for i in string:
        counter = string.count(i)
        times.get(counter).append(string.index(i))
    return string[times.get(count)[index - 1]]


char = search()
print(char)



# 8. 判断字符串 a = “welcome to my world” 是否包含单词 b = “world”，包含返回 True，不包含返回 False。

def judge():
    string = input('请输入字符串：')
    word = input('请输入单词：')
    return word in string


print(judge())



# 9. 从 0 开始计数，输出指定字符串 A = “hello” 在字符串 B = “hi how are you hello world, hello yoyo!”中第一次出现的位置，如果 B 中不包含 A，则输出 -1。

# 方法1：
def first_index():
    string = input('请输入字符串：')
    word = input('请输入单词：')
    return string.find(word)


# print(first_index())
'''


# 方法2：
def first_index():
    string = input('请输入字符串：')
    word = input('请输入单词：')
    for i in range(0, len(string) - len(word) + 1):
        if string[i:i + len(word)] == word:
            return i


print(first_index())

# 10. 从 0 开始计数，输出指定字符串 A = “hello”在字符串 B = “hi how are you hello world, hello yoyo!”中最后出现的位置，如果 B 中不包含 A，则输出 -1。

# 将第9题的 find 方法换为 rfind 即可
