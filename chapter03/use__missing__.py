"""
    所有的映射类型在处理找不到的键的时候,都会牵扯到 __missing__方法。这也是这个方法称作
“missing”的原因。虽然基类 dict 并没有定义这个方法,但是 dict 是知道有这么个东西存在的。也
就是说,如果有一个类继承了 dict,然后这个继承类提供了 __missing__ 方法,那么在 __getitem__
碰到找不到的键的时候,Python 就会自动调用它,而不是抛出一个 KeyError 异常。
    __missing__ 方法只会被 __getitem__ 调用(比如在表达式 d[k] 中)。提供 __missing__
方法对 get 或者__contains__(in 运算符会用到这个方法)这些方法的使用没有影响。

Tests for item retrieval using `d[key]` notation::
>>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
>>> d['2']
'two'
>>> d[4]
'four'
>>> d[1]
Traceback (most recent call last):
...
KeyError: '1'
Tests for item retrieval using `d.get(key)` notation::
>>> d.get('2')
'two'
>>> d.get(4)
'four'
>>> d.get(1, 'N/A')
'N/A'
Tests for the `in` operator::
>>> 2 in d
True
>>> 1 in d
False

    如果要自定义一个映射类型,更合适的策略其实是继承collections.UserDict 类。这里我们从
dict 继承,只是为了演示 __missing__ 是如何被dict.__getitem__ 调用的。
"""


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            # 如果找不到的键本身就是字符串,那就抛出 KeyError 异常。
            raise KeyError(key)
        # 如果找不到的键不是字符串,那么把它转换成字符串再进行查找。
        # return self[str(key)]

    def get(self, key, default=None):
        try:
            # get 方法把查找工作用 self[key] 的形式委托给 __getitem__,这样在宣布查找
            # 失败之前,还能通过 __missing__ 再给某个键一个机会。
            return self[key]
        except KeyError:
            # 如果抛出 KeyError,那么说明 __missing__ 也失败了,于是返回 default。
            return default

    # def __setitem__(self, key, value):
    #     self[str(key)] = value  # 会递归调用__setitem__，进入无限循环

    def __contains__(self, key):
        # 先按照传入键的原本的值来查找(我们的映射类型中可能含有非字符串的键),如果没找到,
        # 再用 str() 方法把键转换成字符串再查找一次。
        # return key in self or str(key) in self
        #  in dict操作会调用self.__contains__陷入无限循环，所以这里必须使用keys()
        return key in self.keys() or str(key) in self.keys()

"""
    下面来看看为什么 isinstance(key, str) 测试在上面的__missing__ 中是必需的。如果没有
这个测试,只要 str(k) 返回的是一个存在的键,那么__missing__ 方法是没问题的,不管是字符串键还
是非字符串键,它都能正常运行。但是如果 str(k) 不是一个存在的键,代码就会陷入无限递归。这是因
为 __missing__ 的最后一行中的 self[str(key)] 会调用 __getitem__,而这个 str(key) 又不
存在,于是 __missing__又会被调用。为了保持一致性,__contains__ 方法在这里也是必需的。这是
因为 k in d 这个操作会调用它,但是我们从 dict 继承到的 __contains__方法不会在找不到键的时
候调用 __missing__ 方法。__contains__里还有个细节,就是我们这里没有用更具 Python 风格的
方式——k inmy_dict——来检查键是否存在,因为那也会导致 __contains__ 被递归调用。为了避免这一
情况,这里采取了更显式的方法,直接在这个self.keys() 里查询。
    像 k in my_dict.keys() 这种操作在 Python 3 中是很快的,而且即便映射类型对象很庞大也
没关系。这是因为dict.keys() 的返回值是一个“视图”。视图就像一个集合,而且跟字典类似的是,在视
图里查找一个元素的速度很快。
    Python 2 的 dict.keys() 返回的是个列表,因此虽然上面的方法仍然是正确的,它在处理体积大
的对象的时候效率不会太高,因为 k in my_list 操作需要扫描整个列表。
"""
a = StrKeyDict0()
a[1] = 100
print(a[1])
print(1 in a)
