"""
处理UnicodeEncodeError
    多数非 UTF 编解码器只能处理 Unicode 字符的一小部分子集。把文本转
换成字节序列时,如果目标编码中没有定义某个字符,那就会抛出
UnicodeEncodeError 异常,除非把 errors 参数传给编码方法或函
数,对错误进行特殊处理。
    >>> city = 'São Paulo'
    >>> city.encode('cp437') ➌
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
    return codecs.charmap_encode(input,errors,encoding_map)
    UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
    position 1: character maps to <undefined>
    >>> city.encode('cp437', errors='ignore') ➍
    >>> city.encode('cp437', errors='replace') ➎
    b'S?o Paulo'
    >>> city.encode('cp437', errors='xmlcharrefreplace') ➏
    b'São Paulo'
    ❸ 'cp437' 无法编码 'ã'(带波形符的“a”)。默认的错误处理方式
    'strict' 抛出 UnicodeEncodeError。
    ❹ error='ignore' 处理方式悄无声息地跳过无法编码的字符;这样做
    通常很是不妥。
    ❺ 编码时指定 error='replace',把无法编码的字符替换成 '?';数
    据损坏了,但是用户知道出了问题。
    ❻ 'xmlcharrefreplace' 把无法编码的字符替换成 XML 实体。
    注：编解码器的错误处理方式是可扩展的。你可以为 errors 参
    数注册额外的字符串,方法是把一个名称和一个错误处理函数传给
    codecs.register_error 函数。参见 codecs.register_error
    函数的文档
(https://docs.python.org/3/library/codecs.html#codecs.register_error)
"""