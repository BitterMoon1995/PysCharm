import sys
import unittest
from inspect import isgeneratorfunction

'''
一个可迭代的类，只要实现 __iter__() 与 __next__()即可

StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
'''


class MyCtn:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


class IteratorAndGenerator(unittest.TestCase):
    def test_a(self):
        li = list(range(10))
        it = iter(li)
        '''
        迭代器是一个可以记住遍历的位置的对象。
        迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
        迭代器有两个基本的方法：iter() 和 next()。
        '''
        # print(it)
        # print(next(it))
        # print(next(it))

        # 迭代器对象可以使用常规for语句进行遍历
        # for i in it:
        #     print(i, end=' ')

        # 也可以使用 next() 函数
        while True:
            try:
                print(next(it))
            except StopIteration:
                break

        self.assertEqual(1, 1)

    def test_iterable(self):
        myctn = MyCtn()
        it = iter(myctn)
        print(it)
        print(next(it))

        for item in it:
            print(item)

        self.assertEqual(1, 1)

    def test_generator(self):
        print(isgeneratorfunction(fibonacci_generator))
        # 生成器返回迭代器
        fibonacci_iterator = fibonacci_generator(20)
        # fibonacci_iterator()

        next(fibonacci_iterator)

        # while True:
        #     try:
        #         print(next(generator), end=' ')
        #     except StopIteration:
        #         break

        self.assertEqual(1, 1)


'''
一个带有 yield 的函数就是一个 generator（生成器函数），调用generator会返回一个iterator，
该迭代器也被称为该生成器的生成器对象
generator函数与普通函数不同：
1. 调用它时不会执行任何函数内部代码，只会返回一个迭代器
2. 只有执行对应迭代器的next方法时，才会开始执行generator函数
3. generator函数中如果return，会隐式抛出StopIteration异常
'''


def fibonacci_generator(max_):
    print('nigger')
    a, b, count = 0, 1, 0
    while True:
        if count > max_:
            # 此处暗地里抛了 StopIteration
            # 在一个 generator function 中，如果没有 return，则默认执行至函数完毕，
            # 如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
            return
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    unittest.main()
