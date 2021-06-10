import unittest
from math import sqrt

'''
（菜鸟里面没有）
1.四个容器可以相互进行拷贝构造。如果是字典，取key。
'''


class TheList(unittest.TestCase):
    # 列表的数据项不需要具有相同的类型。创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
    # 元素可以重复
    def test_a(self):
        list0 = []
        print(type(list0))
        list4 = [{1, 2, 3}]
        print(type(list4))
        list1 = ['java', True, 'lisp', 4396, 0.2, 1 + 2j, 4396]
        list1[5] = 'sima'
        print(list1)
        print(type(list1))
        # 访问列表中的值：与字符串的索引一样，列表索引从 0 开始
        print(list1[0])
        print(list1[3])
        # 索引也可以从尾部开始，最后一个元素的索引为 -1
        print(list1[-2])
        print(list1[-1])
        self.assertEqual(True, 1)

    def test_cut(self):
        list1 = ['java', 'javascript', 'go', 'c++', 'lisp', 'lua']
        # 左闭右开
        list2 = list1[1:3]
        print(list2)
        print(list1[3:])
        print(list1[:-2])

        self.assertEqual(1, 1)

    def test_append(self):
        list1 = ['java', 'javascript', 'go', 'c++']
        print(id(list1))
        list1.append('python')
        print(id(list1))
        self.assertEqual(1, 1)

    def test_del(self):
        list1 = ['java', 'javascript', 'go', 'c++', 'python']
        del list1[4]
        print(list1)
        self.assertEqual(1, 1)

    def test_operator(self):
        list1 = ['java', 'javascript', 'go', 'c++', 'python']
        # 长度
        print(len(list1))
        # 组合
        l2, l3 = [1, 2, 3], ['a', 'b', 'c']
        # l4 = l2 + l3
        l4 = list1 + l3
        print(l4)
        # 重复
        l5 = l3 * 3
        print(l5)
        # 成员判断
        print('python' in list1)
        self.assertEqual(1, 1)

    def test_functions(self):
        list1 = ['java', 'javascript', 'go', 'c++', 'python', 'c']
        list2 = [1, 2, 3, 4, 5, 6]
        # 函数
        print(max(list1), max(list2), min(list1))  # 最大/小值
        list3 = list((1, 2, 3, 4, 5))  # 将元组转换为列表
        # 方法
        print(list1.count('c'))
        list1.pop(-1)  # 移除元素，可指定索引，默认为-1
        list1.remove('go')
        print(list1)
        list2.reverse()
        print(list2)
        list2.clear()
        list4 = list2.copy()
        print(list4)
        self.assertEqual(1, 1)

    def test_infer_expression(self):
        li1 = [1, 2, 3, 4]
        li2 = [3 * x for x in li1]
        li3 = [sqrt(x) for x in li1]
        print(li2)
        print(li3)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
