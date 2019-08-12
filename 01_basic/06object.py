#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类和实例
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, name):
        self.__sname = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
# print(bart.__name)
print(bart.get_name())


# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(self):
        self.run()
        self.run()


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

b = Animal()
c = Dog()

b.run()
c.run()

print(isinstance(c, Animal))
print(isinstance(c, Dog))

c.run_twice()
