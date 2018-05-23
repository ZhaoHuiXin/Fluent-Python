
a = {"a": 1, "b": 2}
print(a)
a.update([("c", 3)])
print(a)
a.update(dict(zip(['one', 'two'], [11, 22])))
print(a)
