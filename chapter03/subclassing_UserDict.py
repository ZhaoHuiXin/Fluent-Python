"""
    UserDict 并不是 dict 的子类,但是UserDict 有一个叫作 data 的属性,是 dict 的实例,
这个属性实际上是 UserDict 最终存储数据的地方。这样做的好处是,比起示例 3-7,UserDict 的子
类就能在实现 __setitem__ 的时候避免不必要的递归,也可以让 __contains__ 里的代码更简洁。

Tests in dict:
>>> dict_d = {"china":1 ,"usa":2}
>>> "china" in dict_d
True
>>> "england" in dict_d
False
>>> 1 in dict_d
False
"""
import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

a = StrKeyDict()
a["key1"] = "one"
print(a.keys())
print("key1" in a)
a[1] = 100
print(a[1])
