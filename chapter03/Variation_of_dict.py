"""
    collections.OrderedDict:
    这个类型在添加键的时候会保持顺序,因此键的迭代次序总是一致的。OrderedDict 的 popitem
方法默认删除并返回的是字典里的最后一个元素,但是如果像 my_odict.popitem(last=False) 这样
调用它,那么它删除并返回第一个被添加进去的元素。
    collections.ChainMap:
    该类型可以容纳数个不同的映射对象,然后在进行键查找操作的时候,这些对象会被当作一个整体被逐
个查找,直到键被找到为止。这个功能在给有嵌套作用域的语言做解释器的时候很有用,可以用一个映射
对象来代表一个作用域的上下文。在 collections 文档介绍 ChainMap 对象的那一部分。例：
        import builtins
        pylookup = ChainMap(locals(), globals(), vars(builtins))
    （个人测试：当对ChainMap进行update操作的时候，会作用到ChainMap中的第一个字典）
    collections.Counter:（可以对ChainMap进行操作）
    这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器。所以这个类
型可以用来给可散列表对象计数,或者是当成多重集来用——多重集合就是集合里的元素可以出现不止一次。
Counter 实现了 + 和 - 运算符用来合并记录,还有像most_common([n]) 这类很有用的方法。
most_common([n]) 会按照次序返回映射里最常见的 n 个键和它们的计数。例：
        >>> ct = collections.Counter('abracadabra')
        >>> ct
        Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
        >>> ct.update('aaaaazzz')
        >>> ct
        Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
        >>> ct.most_common(2)
        [('a', 10), ('z', 3)]
    collections.UserDict:
    这个类其实就是把标准 dict 用纯 Python 又实现了一遍。跟 OrderedDict、ChainMap 和
Counter 这些开箱即用的类型不同,UserDict 是让用户继承写子类的。下面就来试试。
"""