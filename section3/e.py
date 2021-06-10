import unittest


def typed_func(a: int, s: str) -> float:
    print(a)
    print(s)
    return 43.96

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def single_asterisk(name, *infos):
    # print(type(infos))
    print(name)
    print(infos)


# 如果单独出现星号 * 后的参数必须用关键字传入。
def single_asterisk2(*, name):
    print(name)


def two_asterisk(**nigger_infos):
    print(nigger_infos)


sum_ = lambda a, b: a + b


class FunctionAdvanced(unittest.TestCase):
    """
    typing --- 类型提示支持   3.5+
    可注解函数的参数与返回类型
    Python 运行时不强制执行函数和变量类型注解，但这些注解可用于类型检查器、IDE、静态检查器等第三方工具。
    """

    def test_typing(self):
        typed_func(1, '尼哥死妈')
        self.assertEqual(1, 1)


    def test_variable_params(self):
        single_asterisk('nigger', 25, 2000)
        single_asterisk('Franklin', 22)
        single_asterisk2(name='lama')
        self.assertEqual(1, 1)

    def test_two_asterisk(self):
        two_asterisk(name='尼哥', age=22)
        self.assertEqual(1, 1)

    def test_lambda_func(self):
        print(sum_(1, 2))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
