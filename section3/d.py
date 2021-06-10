import unittest


def my_max(a, b):
    if a > b:
        return a
    return b


def mutable_t(ctn, v):
    if isinstance(ctn, dict):
        ctn.pop(v)
        return
    ctn.remove(v)


def immutable_t(x):
    if isinstance(x, tuple):
        del x
        return
    if isinstance(x, str):
        x += ' black slave'
        return
    x += 10


def print_info(name, age):
    print(name)
    print(age)


def default_param(age, name='尼哥黑奴', ):
    print(name)
    print(age)


class TheFunction(unittest.TestCase):

    def test_a(self):
        print(my_max(1, 9))
        self.assertEqual(1, 1)

    '''
    python 函数的参数传递：
    可变类型：类似 C++ 的引用传递，如 列表、集合、字典
    不可变类型：类似 C++ 的值传递，如整数、字符串、元组
    '''

    def test_mutable(self):
        li = [1, 3, 5]
        set_ = {1, 3, 5}
        dic = {1: 'nigger', 3: 'black slave', 5: 'nigger slave'}
        mutable_t(set_, 5)
        mutable_t(li, 5)
        mutable_t(dic, 5)
        print(set_)
        print(li)
        print(dic)
        self.assertEqual(1, 1)

    def test_immutable(self):
        tup = (1, 3, 5)
        immutable_t(tup)
        print(tup)
        i = 10
        s = 'nigger'
        immutable_t(i)
        immutable_t(s)
        print(i)
        print(s)
        self.assertEqual(1, 1)

    def test_whether_specify_args(self):
        # 调用时不指定参数名，就得注意参数顺序
        print_info('尼哥', 20)

        # 如果指定参数名，顺序就任意
        print_info(age=22, name='nigger slave')
        self.assertEqual(1, 1)

    # cxx风格的默认参数语法规则
    def test_defaultParam(self):
        default_param(20)
        default_param(80, '老黑鬼黑奴')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
