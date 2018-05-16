# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo_info = ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

"""_fields 类属性、 类方法_make(iterable) 和 实例方法 _asdict()"""

columns = City._fields
tokyo = City._make(tokyo_info)
tokyo._asdict()
