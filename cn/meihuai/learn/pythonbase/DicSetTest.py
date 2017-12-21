#!/usr/bin/env python3
# -*- coding: utf-8 -*-
dic = {"Micheal": 95, "Bob": 75, "Tracy": 85}
print(dic["Bob"], "kk not in dic is", "kk" in dic, "Bob IN dic is", "Bob" in dic)
dic['KK'] = abs(98)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(dic.get("a"), dic, dic.get('a', -1))
# 注意：返回None的时候Python的交互环境不显示结果。
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
dic.pop("Bob")
print("after pop bob is ", dic)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

# Set Collection,set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print("set is ", s)
s = set([1, 2, 2, 3, 4, 4])
print("unique set's character is ", s)
s.add(5)
s.add(10)
print("s add some element is ", s)
tp = (1,2,3)
dic[tp] = 3
print("dic tp is ", dic)
# 这个tuple里面含有可变的list集合所以不能够给dic使用
# tp = (1,[2,3],4)
dic[tp] = 5
print("dic tp is ", dic)
s.remove(10)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print("intersection = ", s1 & s2)
print("union set= ", s1 | s2)
# list集合可变
a = ['a', 'b', 'c']
a.sort()
print(a)
str = 'abc'
change = str.replace('a', "A")
print("str =", str, "change = ", change)
