import math
import unittest
from random import random


class ConditionalStatement(unittest.TestCase):
    """
    注意：
    1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
    3、在Python中没有switch – case语句。只有if
    """

    def test_a(self):
        l1 = [1, 3, 5, 7, 9]
        if 4396 in l1:
            print('有明凯')
        elif l1.count(2800) != 0:
            print('有简自狗')
        else:
            print('gala，游泳滴神！')
        self.assertEqual(1, 1)

    # 如果子句只有一句，其实可以不换行
    def test_singleStm(self):
        num = 4396
        if num == 4396: print('明凯死妈')
        self.assertEqual(1, 1)

    def test_nested(self):
        num = int(input('nigga请输入一个数字：'))
        if num % 2 == 0:
            if num % 3 == 0:
                print('您输入的数字可以被2和3整除')
            else:
                print('您输入的数字可以被2整除，但不能被3整除')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
