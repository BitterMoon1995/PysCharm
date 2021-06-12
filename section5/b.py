import json
import unittest

"""
JSON            Python
object          dict
array           list
array           tuple
【我拒绝】        set
【我拒绝】        range
string          str
【我拒绝】        bytes
number          (int)int
number (real)   float
true            True
false           False
null            None
"""


class Json(unittest.TestCase):
    def test_a(self):
        print(json.dumps(2800))
        print(json.dumps(89.64))
        print(json.dumps('nigger'))
        print(json.dumps('尼哥'))
        # TypeError: Object of type bytes is not JSON serializable
        # print(json.dumps(bytes(233)))
        print(json.dumps(None))
        print(json.dumps(True))

        print(json.dumps(['a', 'b', 'c', '1', 4396]))
        print(json.dumps(('a', 'b', 'c', 6324, '8848')))
        # TypeError: Object of type range is not JSON serializable
        # print(json.dumps(range(10)))
        # TypeError: Object of type set is not JSON serializable
        # print(json.dumps({'a', 'b', 'c'}))

        print(json.dumps({'a': '尼哥', 2: '聚聚', 2.8: 4396}))
        self.assertEqual(1, 1)

    # """
    # 为了正确地猴出中文的JSON，需要了解dumps方法的明细使用方法
    # ensure_ascii：如果 ensure_ascii 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。
    # 如果 ensure_ascii 是 false，这些字符会原样输出。
    # """

    def test_cn_support(self):
        s = '尼哥儿'
        print(json.dumps({1: '黑鬼', 2: '尼哥'}, ensure_ascii=False))
        print(json.dumps(s, ensure_ascii=False))
        self.assertEqual(1, 1)

    def test_other_dumps_args(self):
        arr = ['尼哥', '黑人', '黑奴', '黑鬼']
        print(json.dumps(arr, ensure_ascii=False))
        print(json.dumps(arr, indent=2, ensure_ascii=False))

        dic = {'name': 'Jack', 'race': 'NIGGER', 'age': 22}
        print(json.dumps(dic, separators=('*', '-')))
        self.assertEqual(1, 1)

    # 使用loads反序列化JSON数据
    def test_deserialize(self):
        json_tup = json.dumps(('black', 'nigger', 'slave'))
        dsl_arr = json.loads(json_tup)
        print(dsl_arr, type(dsl_arr))

        dic = {'name': 'Jack', 'race': 'NIGGER', 'age': 22}
        json_dic = json.dumps(dic)
        dsl_dic = json.loads(json_dic)
        print(dsl_dic, type(dsl_dic))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
