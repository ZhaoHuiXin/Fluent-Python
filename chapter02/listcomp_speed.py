# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao
"""
timeit.repeat(stmt='pass', setup='pass',
timer=<default timer>, repeat=3, number=1000000)

创建一个 Timer 实例，参数分别是 stmt（需要测量的语句或函数），
setup（初始化代码或构建环境的导入语句），
timer（计时函数），
repeat（重复测量的次数），
number（每一次测量中语句被执行的次数）
"""
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    # res = timeit.timeit(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))  # *拆包
    # print(label, *('{}'.format(res)))


clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')