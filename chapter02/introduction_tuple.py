# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao

"""可以用 * 运算符把一个可迭代对象拆开作为函数的参数"""
t = (20, 8)
print(divmod(*t))  # Return the tuple (x//y, x%y),Invariant: div*y + mod == x
