import unittest


class TheSet(unittest.TestCase):
    def test_a(self):
        # 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
        set0 = set()
        print(type(set0))
        # 与列表区别：①元素无序 ②且不可重复 ③而且没有索引
        set1 = {'apple', 'samsung', 'huawei', 'huawei'}
        print(set1)
        set2 = set('abcdefg')
        print(set2)
        self.assertEqual(1, 1)

    # 集合间运算
    def test_operate(self):
        set1 = set('abcdefg')
        set2 = set('efghijk')
        print(set1 - set2)  # 差集
        print(set1 | set2)  # 并集
        print(set1 & set2)  # 交集
        print(set1 ^ set2)  # 反交集
        self.assertEqual(1, 1)

    def test_add(self):
        # 1.add
        set1 = {'a', 'b', 'c'}
        # set1.add({'d'})
        set1.add('d')
        print(set1)
        set1.discard('d')
        # 2.update
        # 参数为Iterable[_T]，即任意容器
        set1.update({'d'})
        set1.update(['e'])
        set1.update(tuple('f'))
        # 不难看出如果传入字典，则只会记录Key
        set1.update({'g': 'nigger'})
        print(set1)
        # 还可以同时狂暴轰入多个容器
        set1.update({'h', 'i'}, ('j', 'k'), ['l', 'm'], {'o': 'nigga', 'q': 'slave'})
        print(set1)
        self.assertEqual(1, 1)

    def test_delete(self):
        # 1.remove
        set1 = {'Google', 'Oracle', 'Microsoft', 'Facebook', 'Huawei'}
        # remove删除不存在的元素会报错
        # set1.remove('niggerCompany')
        # 2.discard
        # discard则不会
        set1.discard('niggerCompany')
        set1.discard('Huawei')
        # 3.pop
        # 因为集合没有索引也没有顺序，所以是随机选择幸运儿
        set1.pop()
        print(set1)
        self.assertEqual(1, 1)

    def test_otherBuiltinMethods(self):
        # len clear in copy...
        set1 = set('abcdefg')
        set2 = set('efghijk')
        set3 = set('efg')
        # 是否不相交
        print(set1.isdisjoint(set2))
        # 是否是子集
        print(set3.issubset(set1))
        # 是否是父集
        print(set2.issuperset(set2))
        # 返回两个集合中不重复的元素集合。
        print(set1.symmetric_difference(set2))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
