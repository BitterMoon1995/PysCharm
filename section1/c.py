import math
import unittest
from random import random



class TheNumber(unittest.TestCase):
    def test_type_alias(self):
        self.assertEqual(1, 1)

    def test_treeType(self):
        # 数据类型是不允许改变的, 这就意味着如果改变数字数据类型的值，将重新分配内存空间。
        a = 1  # 整型 int
        b = 0.98  # 浮点型 float
        c = 7 + 3j  # 虚数 complex。有两种写法
        c2 = complex(3, 4)
        print(c2)
        # del a, b, c, c2  # 可以通过使用del语句删除单个或多个对象的引用
        # print(a)
        self.assertEqual(1, 1)

        # 使用type()获取数据类型。 不难看出同是数字，亦有不同
        print(type(a), type(b), type(c))

    # 进制
    def test_system(self):
        print("0b1111：", 0b1111)  # 二进制
        print("0xa0f：", 0xa0f)  # 十六进制
        print("0o37：", 0o37)  # 八进制

        a = 10
        b = 20
        a2 = bin(a)  # 10转2
        b16 = hex(b)  # 10转16
        print("10：", a2, "20：", b16)
        self.assertEqual(1, 1)

    def test_typeConvert(self):
        a = 5
        b = 89.64
        a2 = float(a)
        b2 = int(b)
        print(a2, b2)
        self.assertEqual(1, 1)

    def test_numFunc(self):
        print(math.ceil(89.64))  # ceiling：n. 天花板；上限
        print((1 > 2) - (1 < 2))
        print(max(63.24, 55))
        print(round(89.46))
        print(round(1.63244396, 3))  # 四舍五入，且舍去3位之后的
        self.assertEqual(1, 1)

    def test_randomNum(self):
        print(random())
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
