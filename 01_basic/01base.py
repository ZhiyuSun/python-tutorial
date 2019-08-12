#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。


# 数据类型
print('I\'m ok.')
print('\\\t\\')
print('\\\n\\')
print('''line1
line2
line3''')
print(3 > 2)
print(True and False)
print(None)
PI = 3.14159265359
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 字符串
print(len('ABC'))
print(len('中文'))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print("{1} {0} {1}".format("hello", "world"))
print("网站名：{name}, 地址 {url}".format(name="百度", url="www.baidu.com"))
site = {"name": "百度", "url": "www.baidu.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 列表
classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)
print(classmates[2])
print(classmates[-1])
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = 'Sarah'
print(classmates)
classmates.append('Tom')
print(classmates)
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']

# 元组
classmates = ('Michael', 'Bob', 'Tracy')
# classmates[0] = 'Tom'

# 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d)
print(d.get('Bob'))
d.pop('Bob')
d.update({'Jerry': 60})
print(d)
# print(d['sun'])

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# set
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
