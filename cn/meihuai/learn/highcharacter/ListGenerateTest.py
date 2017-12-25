#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
list1 = list(range(1, 11))
print("list1 = ", list1)

# 生成1*1, 2*2, 3*3, 4*4
L = []
for x in range(1, 11):
    L.append(x * x)
print("the result L is ", L)

# 列表生成式
xl = [x * x for x in range(1, 11)]
print("xl =", xl)
x2 = [x * x for x in range(1, 11) if x % 2 == 0]
print("x2 =", x2)
mn = [m + n for m in "ABC" for n in "XYZ"]
print("m + n is ", mn)


listFiles = [d for d in os.listdir('.')]
print("listFiles is ", listFiles)
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in d.items():
    print(k, '=', v)

