#!/usr/bin/emv python3
# -*- coding: utf-8 -*-
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n


def factor(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factor(n - 1)


print(factor(700))  # max stack depth
print(factor(0))  # max stack depth


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def tail_fact(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return fact_iter(n, 1)


# print(tail_fact(3000))

# 斐波那契数列
# f1 = 1 ,f2 = 1 f3 = f1 + f2


def fibonacci(n):
    if n < 0:
        return -1
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))


def curse_fibonacci(n):
    if n < 0:
        return -1
    if n == 1 or n == 2:
        return 1
    f1 = 1
    f2 = 1
    while n >= 3:
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        n = n - 1
    return f3


print(curse_fibonacci(7))
# 1 1 2 3 5 8 13
