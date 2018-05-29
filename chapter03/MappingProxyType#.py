"""
>>> from types import MappingProxyType
>>> d = {1:'A'}
>>> d_proxy = MappingProxyType(d)
>>> d_proxy
mappingproxy({1: 'A'})
>>> d_proxy[1]
'A'
>>> d_proxy[2] = 'x'
Traceback (most recent call last):
File '<stdin>', line 1, in <module>
TypeError: 'mappingproxy' object does not support item assignment
>>> d[2] = 'B'
>>> d_proxy
mappingproxy({1: 'A', 2: 'B'})
>>> d_proxy[2]
'B'
>>>
"""

from types import MappingProxyType

origin_dict = {"a": 100, "b": 200}
use_dict = MappingProxyType(origin_dict)
print(use_dict)
print(use_dict.keys())
print(type(use_dict))