# -*- coding=utf8 -*-
#
# Copyright @ 2018 HuiXin Zhao
import array
"""
    memoryview 是一个内置类,它能让用户在不复制内容的情况下操作同一个数组的不同切片。
    When should a memoryview be used ?
    内存视图其实是泛化和去数学化的 NumPy 数组。它让你在不需要复制内容的前提下,在数据结构之
间共享内存。其中数据结构可以是任何形式,比如 PIL 图片、SQLite 数据库和 NumPy 的数组,等等。
这个功能在处理大型数据集合的时候非常重要。
"""
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(type(memv), memv, len(memv))
for i in memv:
    print(i)
print(memv[0])
memv_oct = memv.cast('B')
"""这里备注下：2字节有符号intger'h'转1字节无符号'B'，0代表+，255代表-，值为255+1-x"""
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

