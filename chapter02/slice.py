# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao

"""一个众所周知的秘密是,我们还可以用 s[a:b:c] 的形式对 s 在 a 和 b
之间以 c 为间隔取值。c 的值还可以为负,负值意味着反向取值。"""

# 给切片命名
one_to_three = slice(0, 3)
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ONE_THREE = num_list[one_to_three]
print(ONE_THREE)


"""如果赋值的对象是一个切片,那么赋值语句的右侧必须是个可迭代
对象。即便只有单独一个值,也要把它转换成可迭代的序列。"""
test_list = list(range(10))
test_list[2: 5] = [100]
