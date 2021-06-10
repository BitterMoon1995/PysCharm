import unittest
from dataclasses import dataclass


class Woman:
    ex_bf_num = 10
    # 父类的私有属性不会被继承
    __orgasm_time = 500

    # 父类的构造、析构不会被隐式调用
    def __init__(self, ex_bf_num):
        print('女人构造')
        self.ex_bf_num = ex_bf_num

    def __del__(self):
        print('女人被前夫鲨了')

    def wear_dress(self):
        print('女人穿裙')

    # 父类的私有方法无法被重写
    def __suck_dick(self):
        print("女人含屌")


class Girl(Woman):
    """
    类的私有属性
    __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
    在类内部的方法中使用时 self.__private_attrs。
    """
    __weight = 102

    # def __init__(self):
    #     print('nigga')

    # 定义构造方法
    def __init__(self, name, age, ex_bf_num):
        super().__init__(ex_bf_num)
        print('女孩构造')
        self.name = name
        self.age = age

    # 析构函数，释放对象时使用
    def __del__(self):
        super().__del__()
        print('女孩子偷体育生被男友持刀捉奸，这下糟了')

    """
    类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称,
    按照惯例它的名称是 self。代表的是类的实例。
    """

    def hello(self):
        print(f'我是骚骚{self.name}')
        print(self.__class__)

    def wear_dress(self):
        print('小骚骚穿骚JK')

    """
    定义类方法和静态方法。
    区别是静态方法可以不需要传入任何参数，类方法还得带上cls
    """

    @staticmethod
    def diao_kai_zi():
        print('女孩子静态方法之钓凯子')

    @classmethod
    def gou_shuai_ge(cls):
        print('女孩子类方法之勾帅哥')


# @functools.total_ordering
@dataclass
class MonthlyIncome:
    salary: int
    bonus: float
    socialSecurity: float

    def __eq__(self, o: object) -> bool:
        if not type(self) == type(o):
            return False
        else:
            assert isinstance(o, MonthlyIncome), '不可能'
            if self.salary == o.salary and self.bonus == o.bonus and self.socialSecurity == o.socialSecurity:
                return True
            else:
                return False

    def __add__(self, other):
        if not isinstance(other, MonthlyIncome):
            raise ValueError("值错误")
        return MonthlyIncome(self.salary + other.salary,
                             self.bonus + other.bonus, self.socialSecurity + other.socialSecurity)

    def __radd__(self, other):
        if not isinstance(other, MonthlyIncome):
            raise ValueError("值错误")
        return MonthlyIncome(self.salary + other.salary,
                             self.bonus + other.bonus, self.socialSecurity + other.socialSecurity)


class PysOOP(unittest.TestCase):
    def test_a(self):
        girl1 = Girl('吴雨薇', 26, 20)
        girl1.hello()
        print(girl1.age)

        self.assertEqual(1, 1)

    def test_inheritance(self):
        # 始祖巨人
        print('The base class of the class hierarchy：', object)

        girl1 = Girl('吴大骚', 26, 20)
        girl1.wear_dress()
        print(girl1.ex_bf_num)
        self.assertEqual(1, 1)

    def test_class_static_method(self):
        Girl.diao_kai_zi()
        Girl.gou_shuai_ge()
        self.assertEqual(1, 1)

    def test_data_class(self):
        june_income = MonthlyIncome(5000, 2000, 300)
        print(june_income)
        self.assertEqual(1, 1)

    def test_operatorReload(self):
        may_inc = MonthlyIncome(5200, 2000, 300)
        june_inc = MonthlyIncome(5400, 2000, 300)
        july_inc = MonthlyIncome(5400, 2000, 300)
        print(may_inc + june_inc)
        print(may_inc == june_inc)
        print(june_inc == july_inc)

        # 此时may_inc是被加的那个，适用反向加号
        # 如果没有重载反向加号运算符，会报错
        # res = 1 + may_inc

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
