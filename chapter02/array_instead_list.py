from array import array
from random import random

"""
    创建数组需要一个类型码,这个类型码用来表示在底层的 C 语言应该存放怎样的数据类型。比如 b 
类型码代表的是有符号的字符(signed char),因此 array('b') 创建出的数组就只能存放一个字节大
小的整数,范围从 -128 到 127,这样在序列很大的时候,我们能节省很多空间。而且 Python 不会允许
你在数组里存放除指定类型之外的数据。"""
floats = array('d', (random() for i in range(10**7)))
# print(floats)
print(floats[-1])
fp = open('floats.txt', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.txt', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

"""
    a.typecode 返回只有一个字符的字符串,代表数组元素在 C 语言中a.typecode的类型
    从 Python 3.4 开始,数组类型不再支持诸如 list.sort() 这种就地排序方法。要给数组排序
的话,得用 sorted 函数新建一个数组:
    a = array.array(a.typecode, sorted(a))
"""
