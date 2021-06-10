import unittest


class Nigger:
    def __enter__(self):
        print('nigger__enter__调用')
        return '明凯亲妈被黑人操死'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('nigger__exit__调用')


def get_nigger() -> Nigger:
    print('get_nigger()方法调用')
    return Nigger()


class FileOperate(unittest.TestCase):
    """
    w: 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    """

    def test_write(self):
        file = open('ayaka.txt', mode='w')
        file.writelines('老婆神里绫华\n')
        file.writelines('神里绫华老婆\n')
        file.writelines('神里绫华老婆\n')

        file.close()
        self.assertEqual(1, 1)

    """
    flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
    一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
    
    用读写流的时候，其实数据是先被读到了内存中，然后用数据写到文件中，当你数据读完的时候不代表你的数据已经写完了，
    因为还有一部分有可能会留在内存这个缓冲区中。如果此时调用了 close()方法关闭了读写流，那么这部分数据就会丢失，
    所以应该在关闭读写流之前先flush()，先清空数据。这个方法的作用是把缓冲区的数据强行输出。如果你不flush就可能会没有真正输出
    
    文本模式，一般都用默认缓冲区大小
    二进制模式，是一个个字节的操作，可以指定buffer的大小
    一般来说，默认缓冲区大小是个比较好的选择，除非明确知道，否则不调整它
    一般编程中，明确知道需要写磁盘了，都会手动调用一次flush，而不是等到自动flush或者close的时候.
    """

    def test_flush_write(self):
        with open('wife.txt', 'w') as file:
            for i in range(5):
                file.writelines('小阿晴\n')
                file.flush()
        self.assertEqual(1, 1)

    def test_read(self):
        try:
            file = open('ayaka.txt', mode='r')
        except FileNotFoundError:
            print('找不到文件')
            return
        # 无缓冲读
        # s = file.read()
        # print(s)

        # 普通BufferReader
        res = ''
        while True:
            buf = file.read(10)
            print(buf)
            res += buf
            if not buf:
                break

        print(res)
        # res.strip()
        file.close()
        self.assertEqual(1, 1)

    # 配置文件推荐readline
    def test_read_line(self):
        file = open('ayaka.txt', mode='r')
        res = ''
        while True:
            line = file.readline()
            res += line
            if not line:
                break
        print(res)
        file.close()
        self.assertEqual(1, 1)

    # 高雅之妙用关键字with&as
    def test_read_with(self):
        res = ''
        with open('ayaka.txt', mode='r') as file:
            while True:
                buf = file.read(10)
                res += buf
                if not buf:
                    break
        print(res)
        self.assertEqual(1, 1)

    """
    with 工作原理
    （１）紧跟with后面的语句被求值后，返回对象的“–enter–()”方法被调用，这个方法的返回值将被赋值给as后面的变量；
    （２）当with后面的代码块全部被执行完之后，将调用前面返回对象的“–exit–()”方法。
    
    ① 执行with后表达式
    ② 调用表达式返回的对象ro的–enter–()方法
    ③ –enter–()方法的返回值被赋值给as后的变量
    ④ 执行with内代码块
    ⑤ 调用ro的–exit–()方法
    """

    def test_with_principle(self):
        with get_nigger() as nigger:
            print('with后代码块执行')

        print('\nnigger值为：', nigger)
        self.assertEqual(1, 1)

    def test_append(self):
        with open('wife.txt', 'a') as file:
            for i in range(5):
                file.write('甘雨！！！\n')
                file.flush()

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
