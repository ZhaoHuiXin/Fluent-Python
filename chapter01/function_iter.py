# -*- coding: utf-8 -*-
# Copyright @ 2018 HuiXin Zhao

from random import randint


def d6():
    return randint(1, 6)


'''
    iter 函数还有一个鲜为人知的用法:传入两个参数,使用常规的函数或任何可调用的对象创建迭代器
。这样使用时,第一个参数必须是可调用的对象,用于不断调用(没有参数),产出各个值;第二个值是哨符,
这是个标记值,当可调用的对象返回这个值时,触发迭代器抛出 StopIteration 异常,而不产出哨符。
    这里的 iter 函数返回一个 callable_iterator 对象。示例中的 for 循环可能运行特别长的
时间,不过肯定不会打印 1,因为 1 是哨符。与常规的迭代器一样,这个示例中的 d6_iter 对象一旦耗
尽就没用了。如果想重新开始,必须再次调用 iter(...),重新构建迭代器。
'''
d6_iter = iter(d6, 1)
for roll in d6_iter:
    print(roll)
