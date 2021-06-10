import unittest


class TheTuple(unittest.TestCase):
    """
    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号 ( )，列表使用方括号 [ ]。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    也可以不要括号
    """

    def test_a(self):
        tuple0 = ()
        print(type(tuple0))
        tuple1 = ('google', 'amd', 'vdos', 1, 2, 3)
        # 不加括号
        tuple2 = 'niggers', 'pigs', 'dogs'
        print(type(tuple2))
        # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
        # x = (1)
        # print(type(x))
        tuple3 = (4396,)
        self.assertEqual(1, 1)

    # 访问、截取，同列表

    # 不允许修改、删除、新增
    def test_unmodifiable(self):
        tuple1 = ('apple', 'amd', 'DJI', 'vdos')
        print(tuple1[3])
        # 修改元组元素操作是非法的
        # tuple1[0] = 'huawei'
        # tuple1[4] = 'google'

        # del tuple1[0]
        # tuple1.remove('apple')
        # tuple1.pop()

        # 但是可以通过截取、拼接，创建新的元组
        tuple2 = ('huawei',) + tuple1[1:]
        print(tuple2)
        self.assertEqual(1, 1)

    '''
    所谓元组的不可变指的是元组所指向的内存中的内容不可变。（普通常量指针）
    重新赋值的元组，会绑定到新的对象，而非修改了原来的对象。
    '''

    def test_constPointer(self):
        tup = (1,)
        print(id(tup))
        tup = (2,)
        print(id(tup))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
