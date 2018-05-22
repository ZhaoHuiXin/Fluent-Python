# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo_info = ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

"""_fields 类属性、 类方法_make(iterable) 和 实例方法 _asdict()"""

columns = City._fields
tokyo = City._make(tokyo_info)
t_dict = tokyo._asdict()
print(columns)
print(tokyo)
print(t_dict)
print(t_dict.get("coordinates"))
