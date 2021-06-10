import unittest


class Operators(unittest.TestCase):
    # 算术运算符   + - * / %略
    def test_arithmeticOp(self):
        # 幂 计算多少次方
        print(2 ** 3)
        # 取整除 先除，然后【向下】取整
        print(9 // 2)
        self.assertEqual(1, 1)

    # 赋值运算符   = +=......略
    def test_assignOp(self):
        """
        毁三观之”海象运算符“ :=
        3.8后开始支持，在表达式内部(流程控制语句中)为变量赋值。
        在下方实例中，可避免len(s)被多次调用
        """
        s = 'nigger'
        if (a := len(s)) >= 3:
            print(a)
            print('大于')
        self.assertEqual(1, 1)

    # 逻辑运算符
    def test_logicOp(self):
        a, b = True, False
        if a and b:
            print('变量 a 和 b 都为 true')
        else:
            print('变量 a 和 b 有一个不为 true')
        if a or b:
            print('变量 a 和 b 至少一个为 true')
        else:
            print('变量 a 和 b 都不为 true')
        if not a:
            print('变量a取非为true')
        else:
            print('变量a取非不为true')

        self.assertEqual(1, 1)

    # 成员运算符 判断在指定的序列中能否找到值
    def test_memberOp(self):
        a, b = 10, 2800
        list1 = [1, 2800, 3, 4396, 5, 6324]
        print(a in list1)
        print(b in list1)
        print(6324 not in list1)
        print(4396 not in list1)

        self.assertEqual(1, 1)

    # 身份运算符 判断用于比较两个对象的存储单元（是不是引用自同一/不同对象）
    def test_IDop(self):
        a = 10
        b = 10
        print(a is b)
        # 注： id()函数用于获取对象内存地址
        print(id(a) is id(b))
        print(id(a), id(b))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
