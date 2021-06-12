import unittest


# range 类型表示不可变的数字序列，通常用于在 for 循环中循环指定的次数。
class Range(unittest.TestCase):
    """
    range 构造器的参数必须为整数（可以是内置的 int 或任何实现了 __index__ 特殊方法的对象）。
    如果省略 step 参数，其默认值为 1。 如果省略 start 参数，其默认值为 0，如果 step 为零则会引发 ValueError。

    range 类型相比常规 list 或 tuple 的优势在于一个 range 对象总是占用固定数量的（较小）内存，
    不论其所表示的范围有多大（因为它只保存了 start, stop 和 step 值，并会根据需要计算具体单项或子范围的值）。
    """

    def test_cst(self):
        r1 = range(10)
        print(type(r1))
        print(r1)
        print(list(r1))
        r2 = range(1, 10)
        print(list(r2))
        r3 = range(1, 10, 2)
        print(list(r3))

        self.assertEqual(1, 1)

    # range 对象实现了 collections.abc.Sequence ABC，提供如包含检测、元素索引查找、切片等特性，并支持负索引
    def test_impl_of_Sequence(self):
        r = range(0, 20, 2)
        print(list(r))
        print(1 in r)
        print(2 in r)
        print(r[5])
        print(list(r[:6]))
        print(r[-1])
        self.assertEqual(1, 1)

    """
    使用 == 和 != 检测 range 对象是否相等是将其作为序列来比较。 
    也就是说，如果两个 range 对象表示相同的值序列就认为它们是相等的。
     （请注意比较结果相等的两个 range 对象可能会具有不同的 start, stop 和 step 属性，
     例如 range(0) == range(2, 1, 3) 而 range(0, 3, 2) == range(0, 4, 2)。）
    """

    def test_compare(self):
        print(range(0, 9, 4) == range(0, 11, 4))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
