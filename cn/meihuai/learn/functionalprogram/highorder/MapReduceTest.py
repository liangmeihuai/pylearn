#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import reduce


def f(x):
    return x * x


r = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("r = ", r)

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    L.append(f(n))
print(L)


print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# reduce function reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


print("s.strip is ", ''.strip())
print('dedeEEDe' and 'fede'.strip())
