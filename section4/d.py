import os
import unittest


class OS(unittest.TestCase):
    def test_a(self):
        # 不仅执行命令而且返回执行后的信息对象(常用于需要获取执行命令后的返回信息)，是通过一个管道文件将结果返回
        pipe = os.popen(R'cd')
        print(pipe.read())
        pipe.close()

        # 在子终端运行系统命令，可以获取命令执行后的返回信息以及执行返回的状态
        # res = os.system(R'md d:\mp3')
        # print(res)
        self.assertEqual(1, 1)

    def test_b(self):
        res = ''
        with os.popen(R'md d:\mp3') as pipe:
            while True:
                buf = pipe.readline()
                res += buf
                if not buf:
                    break
        print(res)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
