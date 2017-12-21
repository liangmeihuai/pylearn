#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L = ["Mike", "Luke", "Nancy", "Mary", "Jack"]
r = []
n = 3
for x in range(n):
    r.append(L[x])
print(r)

print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-2:-1])
L = list(range(100))
print(L[:10])
# 前10个数，没两个取一个
print(L[:10:2])
# 所有数，每五个取一个
print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
copy = L[:]
print(copy)
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
