#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 27
if age >= 18 and (age <= 30):
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = [1,2]
if x:
    print("not null")
print(0 and 4)
# python的and和or是位运算符，相当于java的 | &
#  and与or的优先级并不相等，而是and 的优先级高于or
# s = input("birth :")
# birth = int(s)
# if birth > 2000:
#     print("00后")
# else:
#     print("非00后")

