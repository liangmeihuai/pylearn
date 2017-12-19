#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy']
print("classmates = ", classmates)
print("len(classmates)=", len(classmates))
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print("last index of the classmates list is =", classmates[-1])
print("second last index of the classmates list is =", classmates[-2])
classmates.append("Adam")
print("last index of the classmates list is =", classmates[-1])
classmates.insert(1,"Jack")
print("sencond index of the classmates list is =", classmates[1])
# 要删除list末尾的元素，用pop()方法：
val = classmates.pop()
print("classmates = ,val =", classmates, val)
