"""
    “café”这个词可以使用两种方式构成,分别有 4 个和 5 个码位,
但是结果完全一样:
    >>> s1 = 'café'
    >>> s2 = 'cafe\u0301'
    >>> s1, s2
    ('café', 'café')
    >>> len(s1), len(s2)
    (4, 5)
    >>> s1 == s2
    False

    U+0301 是 COMBINING ACUTE ACCENT,加在“e”后面得到“é”。在
Unicode 标准中,'é' 和 'e\u0301' 这样的序列叫“标准等价
物”(canonical equivalent),应用程序应该把它们视作相同的字符。但
是,Python 看到的是不同的码位序列,因此判定二者不相等。
    这个问题的解决方案是使用 unicodedata.normalize 函数提供的
Unicode 规范化。这个函数的第一个参数是这 4 个字符串中的一
个:'NFC'、'NFD'、'NFKC' 和 'NFKD'。下面先说明前两个。
    NFC(Normalization Form C)使用最少的码位构成等价的字符串,而
NFD 把组合字符分解成基字符和单独的组合字符。这两种规范化方式都
能让比较行为符合预期:
    >>> from unicodedata import normalize
    >>> s1 = 'café' # 把"e"和重音符组合在一起
    >>> s2 = 'cafe\u0301' # 分解成"e"和重音符
    >>> len(s1), len(s2)
    (4,5)
    >>> len(normalize('NFC', s1)), len(normalize('NFC', s2))
    (4, 4)
    >>> len(normalize('NFD', s1)), len(normalize('NFD', s2))
    (5, 5)
    >>> normalize('NFC', s1) == normalize('NFC', s2)
    True
    >>> normalize('NFD', s1) == normalize('NFD', s2)
    True
    西方键盘通常能输出组合字符,因此用户输入的文本默认是 NFC 形
式。不过,安全起见,保存文本之前,最好使用 normalize('NFC',
user_text) 清洗字符串。NFC 也是 W3C 的“Character Model for the
World Wide Web: String Matching and Searching”规范
(https://www.w3.org/TR/charmod-norm/)推荐的规范化形式。
"""