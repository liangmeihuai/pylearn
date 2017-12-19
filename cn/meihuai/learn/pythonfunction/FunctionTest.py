#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = abs
print(a(-1))


def my_abs(x):
    if x >= 0:
        print(x)
    else:
        print(-x)


my_abs(-10)
# 1.必选参数 2.默认参数 3.可变参数


#  5.关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 4.命名关键字
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, job='Engineer', city='Beijing')
# person('Jack', 24, 'Beijing', 'Engineer')

