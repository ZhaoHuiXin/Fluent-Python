# -*-*- coding=utf-8 -*-
#
# Copyright 2018 @ HuiXin Zhao

import bisect
import sys

"""
    bisect(haystack, needle) 在 haystack(干草垛)里搜索needle(针)的位置,该位置满足的
条件是,把 needle 插入这个位置之后,haystack 还能保持升序。也就是在说这个函数返回的位置前面
的值,都小于或 等于 needle 的值。其中 haystack 必须是一个有序的序列。你可以先用
bisect(haystack, needle) 查找位置 index,再用(list)haystack.insert(index, needle) 
来插入新值。但你也可用insort 来一步到位,并且后者的速度更快一些。
"""
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
print(len(HAYSTACK))
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
