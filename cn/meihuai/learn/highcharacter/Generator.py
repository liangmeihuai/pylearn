#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# generator生成器
# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(1, 11))
print("next(g) is ", next(g), next(g))


def fib(max):
    if max <= 0:
        print(0)
        return 0
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return "done"


print(fib(6))


def fib_generator(max):
    if max <= 0:
        yield 0
        return 0
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"


f = fib_generator(6)
print(next(f), next(f), next(f))

g = fib_generator(6)

while True:
    try:
        x = next(g)
        print('g=', x)
    except StopIteration as e:
        print("Generator return value ", e.value)
        break


