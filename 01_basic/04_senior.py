#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L[:10:2])
print(L[::5])
print(L[:])

print('ABCDEFG'[:3])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for key, value in d.items():
    print(key, value)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 列表生成式
print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

# 函数可以是变量
f = abs
print(f(-10))


# map/reduce/filter
def f(x):
    return x*x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


def is_odd(n):
    return n % 2 == 1


print(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


# sorted

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2019-8-12')

now()