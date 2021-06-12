import unittest
from base64 import encode

# 二进制序列内置类型，包括bytes bytearray memoryview


class BinarySequence(unittest.TestCase):
    """
    bytes 对象是由单个字节构成的不可变序列。
    bytes 字面值中只允许 ASCII 字符（无论源代码声明的编码为何）。
    虽然 bytes 字面值和表示法是基于 ASCII 文本的，但 bytes 对象的行为实际上更像是不可变的整数序列，
    序列中的每个值的大小被限制为 0 <= x < 256
    """
    def test_bytes(self):
        bytes01 = bytes(888)
        print(bytes01)

        s = '尼哥'
        utf8_bytes = bytes(s, 'utf-8')
        """
        开头的b表示这是一个bytes类型。\xe4是十六进制的表示方式，它占用1个字节的长度，
        因此”中文“被编码成utf-8后，我们可以数得出一共用了6个字节，每个汉字占用3个，
        """
        print(utf8_bytes, len(utf8_bytes), utf8_bytes[0])
        # 不可修改 TypeError: 'bytes' object does not support item assignment
        # utf8_bytes[0] = 22
        unicode_bytes = bytes(s, 'gbk')
        print(unicode_bytes)
        self.assertEqual(1, 1)

    def test_encode_decode(self):
        """
        可以使用encode()函数对字符串进行编码，转换成二进制字节数据，
        也可用decode()函数将字节解码成字符串；用decode()函数解码，英文可不要用指定编码格式，中文需要指定解码方式
        """
        string = '尼哥必死'
        # 默认编码格式为utf8
        utf8_bytes = string.encode()
        print(utf8_bytes)
        gbk_bytes = string.encode(encoding='gbk')
        print(gbk_bytes)
        s1 = gbk_bytes.decode('gbk')
        print(s1)
        # s2 = gbk_bytes.decode('utf8')
        # print(s2)
        self.assertEqual(1, 1)

    # bytearray 对象是 bytes 对象的可变对应物。
    # 该对象除了 bytes 和 bytearray 操作 中所描述的 bytes 和 bytearray 共有操作之外，还支持 可变 序列操作。
    def test_bytearray(self):
        by_array = bytearray(range(10))
        # ValueError: byte must be in range(0, 256)
        # by_array[0] = 4396
        by_array[0] = 7
        print(by_array)
        ba2 = bytearray.fromhex('2Ef0 F1f2  ')
        print(ba2)
        self.assertEqual(1, 1)
