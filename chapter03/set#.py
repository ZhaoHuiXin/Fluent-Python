"""
to make an empty set:
use set()
don't use {} , {,}
像 {1, 2, 3} 这种字面量句法相比于构造方法(set([1, 2, 3]))要
更快且更易读。后者的速度要慢一些,因为 Python 必须先从 set 这个
名字来查询构造方法,然后新建一个列表,最后再把这个列表传入到构
造方法里。但是如果是像 {1, 2, 3} 这样的字面量,Python 会利用一
个专门的叫作 BUILD_SET 的字节码来创建集合。
set：
s.add(e)   把元素 e 添加到 s 中
s.clear()  移除掉 s 中的所有元素
s.copy()    对 s 浅复制
s.discard(e)  如果 s 里有 e 这个元素的话,把它移除
s.remove(e) 从 s 中移除 e 元素,若 e 元素不存在,则抛出 KeyError 异常
s.__iter__() 返回 s 的迭代器
s.__len__()  len(s)
s.pop() 从 s 中移除一个元素并返回它的值,若 s 为空,则抛出 KeyError 异常
"""
a = set([1, 2, 3])
b = set([3, 4, 5])
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)  # 减去交集剩下的合集
found = len(a & b)
print(found)
found_method2 = len(a.intersection([3, 4, 5, 3, 3]))
print(found_method2)

