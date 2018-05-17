
"""导入精度和性能都比较高的计时器(Python 3.3 及更新的版本中都有这个库)"""
from time import perf_counter as pc
import numpy

t0 = pc()
a = numpy.arange(12)
print(a, type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2][1])
print(a[:, 1])
print(a.transpose())
print(pc()-t0)
