import unittest

# 全局变量
mingkai = 4396


class ActionScope(unittest.TestCase):
    # 只有内置（built-in）、全局（模块内）、局部（函数/类内）作用域，
    # 没有“块级作用域“
    def test_no_block_scope(self):
        if 'nigger':
            msg = 'i`m nigger'
        print(msg)
        self.assertEqual(1, 1)

    def test_global_nonlocal(self):
        # mingkai += 1

        global mingkai
        mingkai += 1
        print(mingkai)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
