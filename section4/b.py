import sys
import unittest

'''
你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
'''


class NiggerError(Exception):

    def __init__(self, info: str) -> None:
        self.info = info

    def __str__(self) -> str:
        return repr(self.info)


def raise_nigger(i: int) -> None:
    if i > 5:
        raise NiggerError('尼哥死妈')


class TheExceptionHandle(unittest.TestCase):
    """
    Python 的语法错误或者称之为解析错，是初学者经常碰到的
    即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
    大多数的异常都不会被程序处理，都以错误信息的形式展现
    """

    def test_runtime_error(self):
        # ZeroDivisionError: division by zero
        # a = 1 / 0
        # NameError: name 'bb' is not defined
        # b = bb + 2
        # TypeError: unsupported operand type(s) for +: 'int' and 'str'
        c = 1 + '1'
        self.assertEqual(1, 1)

    def test_try_catch(self):
        while True:
            try:
                x = int(input('请输入一个数字\n'))
                print(x)
                if x == 4396:
                    break
            except ValueError:
                print('检测到输入的不是数字，润了')
                break
        self.assertEqual(1, 1)

    # 完整的try-except-else-finally
    def test_complete_process(self):
        try:
            file = open('nigger.txt')
            line = file.readline()
            i = int(line.strip())
            res = 9 / (i - 7)
            print(res)
        except OSError as e:
            print('打开文件失败')
            print(e)
        except ValueError as e:
            print('转换i:int失败')
        except ZeroDivisionError as e:
            print(e)
            print('除数非法：除以0')
        except NiggerError('尼哥错误') as e:
            print(e)
            raise
        # else 子句将在 try 子句没有发生任何异常的时候执行。
        # 使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。
        # 应在else或finally中定义清理行为
        else:
            file.close()
            print('没有任何异常！')
        # finally 语句无论是否发生异常都将执行最后的代码。
        finally:
            print('可莉小坏宝宝小乖乖')

        self.assertEqual(1, 1)

    def test_raise(self):
        try:
            raise_nigger(6)
        except NiggerError as e:
            # print(e)
            # 可以使用raise将异常再次抛出
            raise
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
