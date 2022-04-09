import unittest
from itertools import count

from Tools.demo.spreadsheet import center


class TheString(unittest.TestCase):
    def test_a(self):
        s0 = ''
        print(type(s0))
        # 我们可以使用引号( ' 或 " )来创建字符串。
        s1 = 'nigger'
        s2 = "nigger slave"
        print(type(s1))
        self.assertEqual(1, 1)

    # Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
    # 使用方括号 [] 来访问或截取字符串， 遵循左闭右开原则
    # 索引值以 0 为开始值。可以为负，-1 为从末尾的开始位置。
    def test_cut(self):
        s = "black nigger slave"
        print(s[0])
        print(s[-2])
        print(s[6:12])
        print(s[6:])
        print(s[:12])
        self.assertEqual(1, 1)

    def test_operator(self):
        s1 = 'black nigger '
        s2 = 'slave'
        print(s1 + s2)
        print('b' in s1)
        # 重复输出
        print(s1 * 3)
        self.assertEqual(1, 1)
        # 原始字符串
        print(R'\n\r\t')
        # 格式化输出
        print("我叫 %s 今年 %d岁 身高%.2f" % ("尼哥", 22, 1.98))

    # 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
    def test_threeQuotation(self):
        html = '''
        <HTML><HEAD><TITLE>
        \n
        Friends CGI Demo</TITLE></HEAD>
        <BODY><H3>ERROR</H3>
        \t<B>%s</B><P>
        <FORM><INPUT TYPE=button VALUE=Back
        ONCLICK="window.history.back()"></FORM>
        </BODY></HTML>
        '''
        print(html)
        self.assertEqual(1, 1)

    '''
    python3.6+  字面量格式化字符串
    f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
    '''

    def test_fString(self):
        s = 'nigger'
        print(f'black {s} slave')
        print(F'{4396 + 1 - 2800}')
        person = {'name': 'Jack·Nigger', 'abode': 'Shandong University '}
        print(f'{person}')
        # 3.8后可以使用 = 符号来拼接运算表达式与结果
        x = 1
        print(f'{++x=}')
        print(f'{s=}')
        self.assertEqual(1, 1)

    # 字符串双引号前加上"r"防止转义
    # 在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转意backslash
    # '\' 。 例如，\n 在raw string中，是两个字符，\和n， 而不会转意为换行符。' \
    # '由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。
    def test_rString(self):
        s1 = r'\tt'
        s2 = '\tt'
        print(s1)
        print(s2)
        self.assertEqual(1, 1)

    # 盘点
    def test_functions(self):
        s0 = '断罪皇女'
        print(s0.center(40, '!'))
        s = 'A man is not old until his regrets take place of his dreams.'
        print(s.count('is'))
        print(s.find('regrets'))
        print(s.replace('man', 'woman'))
        print(s.split(' '))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
