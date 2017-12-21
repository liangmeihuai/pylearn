#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print("k=", k, "v=", v)

for ch in 'ABC':
    print("ch=", ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
strFlag = isinstance('abc', Iterable)
listFlag = isinstance([1, 2, 3], Iterable)
intFlag = isinstance(123, Iterable)
print("strFlag=", strFlag, "listFlag=", listFlag, "intFlag=", intFlag)

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(["A", "B", "C"]):
    print(i, value)

for x in [(1, 1), (2, 4), (3, 9)]:
    print(x)
