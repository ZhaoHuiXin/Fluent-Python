# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao
from time import perf_counter as pc
"""+= 背后的特殊方法是 __iadd__ (用于“就地加法”)。但是如果一个类没有实现这个方法的话,
Python 会退一步调用 __add__ 。"""
start = pc()
l = [1, 2, 3]
print(id(l), l)
l *= 2
print(id(l), l)
print(pc() - start)

again = pc()
# the new tuple has been created
t = (1, 2, 3)
print(id(t), t)
t *= 2
print(id(t), t)
print(pc()-again)
"""
    对不可变序列进行重复拼接操作的话,效率会很低,因为每次都有一个新对象,而解释器需要把原来对
象中的元素先复制到新的对象里,然后再追加新的元素。
    str 是一个例外,因为对字符串做 += 实在是太普遍了,所以 CPython 对它做了优化。为 str
初始化内存的时候,程序会为它留出额外的可扩展空间,因此进行增量操作的时候,并不会涉及复制原有
字符串到新位置这类操作。
"""