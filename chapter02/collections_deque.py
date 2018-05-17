# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao
"""
    双向队列实现了大部分列表所拥有的方法,也有一些额外的符合自身设计的方法,比如说 popleft
和 rotate。但是为了实现这些方法,双向队列也付出了一些代价,从队列中间删除元素的操作会慢一些,
因为它只对在头尾的操作进行了优化。
    append 和 popleft 都是原子操作,也就说是 deque 可以在多线程程序中安全地当作先进先出的
栈使用,而使用者不需要担心资源锁的问题。
"""

from collections import deque

mydq = deque(range(10), maxlen=10)
print(mydq)

mydq.rotate(3)
print(mydq)

mydq.rotate(-4)
print(mydq)

mydq.appendleft(-1)  # append默认为appendright
print(mydq)

mydq.extend([11, 22, 33])
print(mydq)

mydq.extendleft(["a", "b", "c"])
print(mydq)

for i in range(mydq.maxlen):
    print(mydq[i])
