import unittest
import requests


class UrlLib(unittest.TestCase):
    def test_get(self):
        url = 'http://localhost:9000/kv'
        params = {'name': 'nigger'}
        res = requests.get(url, params)
        print(res.content)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
