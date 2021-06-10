import unittest

"""
在 Python 中没有 do..while 循环。只有for 和 while
"""


class LoopStatement(unittest.TestCase):
    # 1.while
    def test_while(self):
        n = 10
        while n > 0:
            print('简自豪死妈')
            n -= 1
        self.assertEqual(1, 1)

    def test_infiniteLoop(self):
        while True:
            num = int(input('请输入：'))
            print('数字为：', num)
        self.assertEqual(1, 1)

    def test_while_else(self):
        n = 0
        while n < 5:
            n += 1
            print(n)
        else:
            print('n>=5了')
        self.assertEqual(1, 1)

    # 2.for
    def test_for_in(self):
        list1 = ['black', 'slave', 'nigger', 'nigger', 'black', 'orangutan']
        for i in list1:
            if i == 'nigger':
                break
            print(i)
        self.assertEqual(1, 1)

    # range
    def test_range(self):
        # for i in range(8):
        #     print(i)

        # 设置区间
        # for i in range(4396, 4399):
        #     print(i)

        # 设置步长
        for i in range(2800, 4396, 200):
            print(i)
        self.assertEqual(1, 1)

    def test_for_in_range(self):
        li = ['Google', 'Apple', 'Oracle', 'Facebook', 'HUAWEI', 'miHoYo', 'Microsoft']
        # 利用range遍历带索引的容器
        for i in range(len(li)):
            print(li[i])
        self.assertEqual(1, 1)

    def test_rang_create_container(self):
        li = list(range(9))
        print(li)
        tu = tuple(range(4396, 4399))
        print(tu)
        set_ = set(range(1, 20, 3))
        print(set_)
        self.assertEqual(1, 1)

    '''
    break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
    continue 语句被用来告诉 Python 【跳过当前循环块中的剩余语句】，然后继续进行下一轮循环。
    '''
    def test_break_continue(self):
        cors = list(range(10))
        for item in cors:
            if item < 5:
                continue
            print(item)
            if item == 8:
                break
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
