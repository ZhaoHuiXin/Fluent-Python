"""创建一个从单词到其出现情况的映射"""
import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

# 把 list 构造方法作为 default_factory 来创建一个 defaultdict
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)
            # 如果 index 并没有 word 的记录,那么 default_factory 会被调
            # 用,为查询不到的键创造一个值。这个值在这里是一个空的列表,然后
            # 这个空列表被赋值给 index[word],继而被当作返回值返回,
            # 因此.append(location) 操作总能成功

for word in sorted(index, key=str.upper):
    print(word, index[word])

""" 注意：
    defaultdict 里的 default_factory 只会在__getitem__ 里被调用,在其他的方法里完全不
会发挥作用。比如,dd 是个 defaultdict, k 是个找不到的键, dd[k] 这个表达式会调用 
default_factory 创造某个默认值,而 dd.get(k) 则会返回 None。所有这一切背后的功臣其实是特
殊方法 __missing__。它会在defaultdict 遇到找不到的键的时候调用 default_factory,而实际
上这个特性是所有映射类型都可以选择去支持的。
"""