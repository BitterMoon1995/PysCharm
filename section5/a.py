import unittest
from typing import *
from dataclasses import dataclass


def any_f(x: Any) -> Any:
    print(x)


myTypeVar = TypeVar('myTypeVar', float, str)


def type_var_f(mtv: myTypeVar) -> None:
    print(mtv)


@dataclass
class Nigger:
    name: str
    age: int


def get_nigger(name: str, age: int) -> Nigger:
    return Nigger(name, age)


def get_nigger_func() -> Callable[[str, int], Nigger]:
    return get_nigger


def union_f(param: Union[str, int]):
    if isinstance(param, str):
        print(param + ' kill nigger')
    else:
        print(param + 20)


def optional_f(param: Optional[float]):
    if type(param) == float:
        print(param + 1.2)
    elif not param:
        print('参数为None')
    else:
        print('参数为其他类型')


class Typing(unittest.TestCase):
    def test_any(self):
        any_f('nigger')
        any_f(8899)
        self.assertEqual(1, 1)

    def test_type_var(self):
        type_var_f(998)
        self.assertEqual(1, 1)

    def test_callable(self):
        gn = get_nigger_func()
        nigger = gn('Jack', 22)
        print(nigger)
        self.assertEqual(1, 1)

    # Union，联合类型，Union[X, Y] 代表要么是 X 类型，要么是 Y 类型。
    def test_union(self):
        union_f(8)
        union_f('godz')
        self.assertEqual(1, 1)

    """
    Optional，意思是说这个参数可以为空或已经声明的类型，即 Optional[X] 等价于 Union[X, None]。
    Optional 并不等价于可选参数，当它作为参数类型注解的时候，不代表这个参数可以不传递，而是说这个参数可以传None，不传也会报错。
    """

    def test_optional(self):
        optional_f(1.2)
        optional_f(None)
        optional_f('w')

        self.assertEqual(1, 1)

    def test_generic(self):
        self.assertEqual(1, 1)
