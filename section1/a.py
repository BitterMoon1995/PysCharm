# 1.变量取别名之as
import unittest as junit

# 2.类型取别名
myInt = int


def print_val(a: myInt) -> None:
    print(a)


class AssignStatement(junit.TestCase):
    # 变量与赋值语句
    def test_helloWorld(self):
        print('hello nigger')
        self.assertEqual(True, True)

    def test_variableAssign(self):
        count = 100
        miles = 12.5
        name = 'nigger'
        print(count, miles, name)
        self.assertEqual(1, 1)

    def test_multiAssign(self):
        a = b = c = 4396
        print(a, b, c)
        a, b, c = 6324, 3.14, 'nigga'
        print(a, b, c)
        self.assertEqual(1, 1)

    def test_def_alias(self):
        # 变量、类型都可以取别名
        self.assertEqual(1, 1)


if __name__ == '__main__':
    junit.main()
