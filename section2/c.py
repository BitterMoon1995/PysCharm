import unittest


class TheDictionary(unittest.TestCase):
    def test_a(self):
        # 创建空字典
        dic0 = {}
        print(type(dic0))
        # 字典是一种可变容器模型，且可存储任意类型对象。
        # 键必须是唯一的，但值则不必。
        dic1 = {'name': 'jack', 'race': 'nigger', 1: 'nigger'}
        print(dic1)
        print(type(dic1))
        # 键必须是不可变的，只能是字符串/数字/元组
        dic2 = {'name': 'alice', 'age': 19, 'age': 19, 'race': '大白骚逼'}
        self.assertEqual(1, 1)

    def test_del(self):
        dic = {'name': 'jack', 'age': 23, 'race': 'nigger'}
        # del dic
        # del dic['name']
        dic.clear()
        self.assertEqual(1, 1)

    def test_funcsAndMethods(self):
        dic = {'name': 'dick', 'age': 23, 'race': 'nigger', 'salary': 2000}
        dic2 = dic.copy()
        print(dic2)
        dic3 = dic.fromkeys(dic, '')
        print(dic3)
        print(dic.get('favorite', 'bitches'))
        print(dic.items())
        print(dic.keys())
        dic2.setdefault('favorite', 'weed')
        print(dic2)
        dic3.update(dic2)
        print(dic3)
        print(dic3.values())
        print(dic3.pop('favorite'))
        print(dic3.popitem())
        print(dic3)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
