import unittest

import dress
from girl import *
from section4.a import Girl
from section4.module_stuty import girl


class PysOOP(unittest.TestCase):
    def test_a(self):
        wear_jk()
        lemon = dress.Dress(name='柠檬海盐', type='JK', price=102.5)
        print(lemon)
        self.assertEqual(1, 1)

    def test_dir(self):
        print(dir(girl))
        self.assertEqual(1, 1)

    def test_import_package(self):
        var = Girl('吴雨薇', 26, 20)
        self.assertEqual(1, 1)
