"""
处理UnicodeDecodeError
   不是每一个字节都包含有效的 ASCII 字符,也不是每一个字符序列都是
有效的 UTF-8 或 UTF-16。因此,把二进制序列转换成文本时,如果假
设是这两个编码中的一个,遇到无法转换的字节序列时会抛出
UnicodeDecodeError。
    另一方面,很多陈旧的 8 位编码——如 'cp1252'、'iso8859_1' 和
'koi8_r'——能解码任何字节序列流而不抛出错误,例如随机噪声。
因此,如果程序使用错误的 8 位编码,解码过程悄无声息,而得到的是无用输出。
    乱码字符称为鬼符(gremlin)或 mojibake(文字化け,“变形文本”的日文)
    把字节序列解码成字符串:成功和错误处理
    >>> octets = b'Montr\xe9al' ➊
    >>> octets.decode('cp1252') ➋
    'Montréal'
    >>> octets.decode('iso8859_7') ➌
    'Montrιal'
    >>> octets.decode('koi8_r') ➍
    'MontrИal'
    >>> octets.decode('utf_8') ➎
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:
    invalid continuation byte
    >>> octets.decode('utf_8', errors='replace') ➏
    'Montral'
    
    ❶ 这些字节序列是使用 latin1 编码的“Montréal”;'\xe9' 字节对
    应“é”。
    ❷ 可以使用 'cp1252'(Windows 1252)解码,因为它是 latin1 的有
    效超集。
    ❸ ISO-8859-7 用于编码希腊文,因此无法正确解释 '\xe9' 字节,而且
    没有抛出错误。
    ❹ KOI8-R 用于编码俄文;这里,'\xe9' 表示西里尔字母“И”。
    ❺ 'utf_8' 编解码器检测到 octets 不是有效的 UTF-8 字符串,抛出
    UnicodeDecodeError。
    ❻ 使用 'replace' 错误处理方式,\xe9 替换成了“ ”(码位是U+FFFD),
    这是官方指定的 REPLACEMENT CHARACTER(替换字符),表示未知字符。
"""