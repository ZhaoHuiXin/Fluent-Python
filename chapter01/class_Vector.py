# -*- coding: utf-8 -*-
# Copyright @ 2018 HuiXin Zhao

from math import hypot


class Vector:
    """
    一个简单的二维向量类
    different between __repr__ and __str__:
        __repr__ goal is to be unambiguous
        __str__ goal is to be readable
        Container’s __str__ uses contained objects’ __repr__

    __bool__:
        我们自己定义的类的实例总被认为是真的,除非这个类对__bool__ 或者 __len__ 函数有
    自己的实现。bool(x) 的背后是调用x.__bool__() 的结果;如果不存在 __bool__ 方法,那么
    bool(x) 会尝试调用 x.__len__()。若返回 0,则 bool 会返回 False;否则返回True。
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__会响应控制台
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # __str__只会响应print和str(),如果没有__str__则找__repr__实现print和str()
    # def __str__(self):
    #     return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # def __bool__(self):
    #     return bool(abs(self))
    # Improve:
    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # 使得 n*Vector(x, y)可用，即可以使用乘法交换律
    def __rmul__(self, scalar):
        return self * scalar

