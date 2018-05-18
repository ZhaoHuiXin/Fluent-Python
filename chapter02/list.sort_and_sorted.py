# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao
"""
    list.sort 方法会就地排序列表,也就是说不会把原列表复制一份。这也是这个方法的返回值是
None 的原因,提醒你本方法不会新建一个列表。
    用返回 None 来表示就地改动这个惯例有个弊端,那就是调用者无法将其串联起来。而返回一个新
对象的方法(比如说 str 里的所有方法)则正好相反,它们可以串联起来调用,从而形成连贯接口
(fluent interface)
    与 list.sort 相反的是内置函数 sorted,它会新建一个列表作为返回值。这个方法可以接受任
何形式的可迭代对象作为参数,甚至包括不可变序列或生成器。而不管 sorted 接受的是怎样的参数,它
最后都会返回一个列表。
    不管是 list.sort 方法还是 sorted 函数,都有两个可选的关键字参数。
    reverse 如果被设定为 True,被排序的序列里的元素会以降序输出(也就是说把最大值当作最小值
来排序)。这个参数的默认值是 False。
    key 一个只有一个参数的函数,这个函数会被用在序列里的每一个元素上,所产生的结果将是排序算
法依赖的对比关键字。比如说,在对一些字符串排序时,可以用 key=str.lower 来实现忽略大小写的排
序,或者是用 key=len 进行基于字符串长度的排序。这个参数的默认值是恒等函数
(identity function),也就是默认用元素自己的值来排序。
    可选参数 key 还可以在内置函数 min() 和 max() 中起作用。另外,还有些标准库里的函数也接
受这个参数,像itertools.groupby() 和 heapq.nlargest() 等。
"""
fruits = ['grape', 'raspberry', 'apple', 'banana']
res = sorted(fruits)
print(res)
print(fruits)
fruits.sort()
print(fruits)
print("-"*20)

reverse_fruits = sorted(fruits, reverse=True)
print(reverse_fruits)
print(fruits)
fruits.sort(reverse=True)
print(fruits)


print("-"*20)
# use lambda
sort_by_lambda = sorted(fruits, key=lambda x: len(x))
print(sort_by_lambda)
sort_by_lambda_sa = sorted(fruits, key=lambda x: len(x)
                           if x.startswith("a") else 0)
print(sort_by_lambda_sa)

sort_by_len = sorted(fruits, key=len)
print(sort_by_len)

