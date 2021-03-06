"""
Unicode 标准把字符的标识和具体的字节表述进行了如下的明确区分。
    字符的标识,即码位,是 0~1 114 111 的数字(十进制),在
Unicode 标准中以 4~6 个十六进制数字表示,而且加前缀“U+”。例
如,字母 A 的码位是 U+0041,欧元符号的码位是 U+20AC,高音
谱号的码位是 U+1D11E。在 Unicode 6.3 中(这是 Python 3.4 使用的
标准),约 10% 的有效码位有对应的字符。
    字符的具体表述取决于所用的编码。编码是在码位和字节序列之间
转换时使用的算法。在 UTF-8 编码中,A(U+0041)的码位编码成
单个字节 \x41,而在 UTF-16LE 编码中编码成两个字节
\x41\x00。再举个例子,欧元符号(U+20AC)在 UTF-8 编码中是
三个字节——\xe2\x82\xac,而在 UTF-16LE 中编码成两个字
节:\xac\x20。
    把码位转换成字节序列的过程是编码;把字节序列转换成码位的过程是解码。
    Python 内置了两种基本的二进制序列类型:Python 3 引入的不可变
bytes 类型和 Python 2.6 添加的可变 bytearray 类型。(Python 2.6 也
引入了 bytes 类型,但那只不过是 str 类型的别名,与 Python 3 的
bytes 类型不同。)
    bytes 或 bytearray 对象的各个元素是介于 0~255(含)之间的整
数,而不像 Python 2 的 str 对象那样是单个的字符。然而,二进制序列
的切片始终是同一类型的二进制序列,包括长度为 1 的切片。
    虽然二进制序列其实是整数序列,但是它们的字面量表示法表明其中有
ASCII 文本。因此,各个字节的值可能会使用下列三种不同的方式显
示。
    可打印的 ASCII 范围内的字节(从空格到 ~),使用 ASCII 字符本
    身。
    制表符、换行符、回车符和 \ 对应的字节,使用转义序列
    \t、\n、\r 和 \\。
    其他字节的值,使用十六进制转义序列(例如,\x00 是空字
    节)。
    因此,在示例 4-2 中,我们看到的是 b'caf\xc3\xa9':前 3 个字节
b'caf' 在可打印的 ASCII 范围内,后两个字节则不然。
    除了格式化方法(format 和 format_map)和几个处理 Unicode 数据的
方法(包括casefold、isdecimal、isidentifier、isnumeric、isprintable
和 encode)之外,str 类型的其他方法都支持 bytes 和 bytearray 类
型。这意味着,我们可以使用熟悉的字符串方法处理二进制序列,如
endswith、replace、strip、translate、upper 等,只有少数几个
其他方法的参数是 bytes 对象,而不是 str 对象。此外,如果正则表
达式编译自二进制序列而不是字符串,re 模块中的正则表达式函数也
能处理二进制序列。
    二进制序列有个类方法是 str 没有的,名为 fromhex,它的作用是解
析十六进制数字对(数字对之间的空格是可选的),构建二进制序列:
    >>> bytes.fromhex('31 4B CE A9')
    b'1K\xce\xa9
"""