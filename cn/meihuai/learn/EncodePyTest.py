#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("encode content=", '中文'.encode('utf-8'))
print("decode content = ", b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))
print("ord('A')= ", ord('A'),
      "\nord('中')=", ord('中'),
      "\nchr(65) = ", chr(65),
      "\nchr(25991)=", chr(25991))
# 计算长度
print("len('ABC')=", len('ABC'))
print("len('中文')=", len('中文'))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print("len(b'ABC')=", len(b'ABC'))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87')=", len(b'\xe4\xb8\xad\xe6\x96\x87'))
print("len('中文'.encode('utf-8''))=", len('中文'.encode("utf-8")))
# 格式化运算符
print('Hi, %s, you have $%d.' %('Michael', 1000000))
print('Hello, {0}, 成绩提升了 {1}%'.format('小明', 17.125))
print('Hello, {0}, 成绩提升了 {1:.4f}%'.format('小明', 17.125))
# %%表示百分号
print( 'growth rate: %d%%' % 7)
