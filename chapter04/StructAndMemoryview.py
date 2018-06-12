"""
    struct 模块提供了一些函数,把打包的字节序列转换成不同类型字段
组成的元组,还有一些函数用于执行反向转换,把元组转换成打包的字节序列
。struct 模块能处理 bytes、bytearray 和 memoryview 对象。

    例：使用 memoryview 和 struct 提取一个 GIF 图像的宽度和高度：
    >>> import struct
    >>> fmt = '<3s3sHH' # ➊
    >>> with open('filter.gif', 'rb') as fp:
    ...
    img = memoryview(fp.read()) # ➋
    ...
    >>> header = img[:10] # ➌
    >>> bytes(header) # ➍
    b'GIF89a+\x02\xe6\x00'
    >>> struct.unpack(fmt, header) # ➎
    (b'GIF', b'89a', 555, 230)
    >>> del header # ➏
    >>> del img
    ❶ 结构体的格式:< 是小字节序,3s3s 是两个 3 字节序列,HH 是两个
16 位二进制整数。
    ❷ 使用内存中的文件内容创建一个 memoryview 对象......
    ❸ ......然后使用它的切片再创建一个 memoryview 对象;这里不会复
    制字节序列。
    ❹ 转换成字节序列,这只是为了显示;这里复制了 10 字节。
    ❺ 拆包 memoryview 对象,得到一个元组,包含类型、版本、宽度和
    高度。
    ❻ 删除引用,释放 memoryview 实例所占的内存。
    注意,memoryview 对象的切片是一个新 memoryview 对象,而且不会
复制字节序列。[ 本书的技术审校之一 Leonardo Rochael 指出,如果使
用 mmap 模块把图像打开为内存映射文件,那么会复制少量字节。
"""