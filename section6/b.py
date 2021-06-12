import unittest
import urllib.request
import urllib.parse


class Urllib(unittest.TestCase):
    def test_get(self):
        # 发起一个不携带参数的get请求
        response = urllib.request.urlopen('http://localhost:9000/blank')
        print(response.reason)
        # print(response.status)
        # 调用url属性，可以获取此次请求的地址
        # print(response.url)
        # 请求头
        # print(response.headers)
        # 由于使用read方法拿到的响应的数据是二进制数据，所有需要使用decode解码成utf-8编码
        print(response.read().decode('utf-8'))
        self.assertEqual(1, 1)

    def test_get_with_params(self):
        base_url = 'http://localhost:9000/kv'
        param_dic = {'name': 'god周', 'wife': '神里绫华'}
        param_str = urllib.parse.urlencode(param_dic)
        print(param_str)
        url = base_url + '?' + param_str
        resp = urllib.request.urlopen(url)
        print(resp)
        decoded_resp = resp.read().decode('utf-8')
        print(decoded_resp)
        self.assertEqual(1, 1)

    def test_post(self):
        base_url = 'http://localhost:9000/kv_post'
        param_dic = {'name': 'god周', 'wife': '神里绫华'}
        query_str = urllib.parse.urlencode(param_dic)
        # 将序列化后的字符串转换成二进制数据，因为post请求携带的是二进制参数
        byte_data = bytes(query_str, 'utf-8')
        # 如果给urlopen这个函数传递了data这个参数，那么它的请求方式则不是get请求，而是post请求
        resp = urllib.request.urlopen(base_url, data=byte_data)
        dec_resp = resp.read().decode('utf-8')
        print(dec_resp)

        self.assertEqual(1, 1)
