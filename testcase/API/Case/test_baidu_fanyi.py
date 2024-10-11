# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: test_baidu_fanyi.py
# @Time: 2021/3/13 11:30
# @Author: sun

import os
import unittest
import ddt
import random
import json
import requests
from time import sleep
from Comm.data import read_excel
from Comm.encryption import make_md5
from conf.config import CASE_DIR
from APIs.base_api import BaseAPI, check_result


# 开通普通个人的百度翻译接口，设置appid和appkey.
app_id = '20210313000725421'
app_key = 'ro3HGgrEp7V1_EfvXdQe'

# 获取测试数据
file = os.path.join(CASE_DIR, 'API', "Testdata", "baidu_fanyi.xlsx")
test_data = read_excel(file)
api = 'APIs.fanyi.baidu'


@ddt.ddt
class TestBaiduFanyi(unittest.TestCase):
    """百度翻译接口测试"""

    def setUp(self):
        self.api = BaseAPI(api)

    @ddt.data(*test_data)
    def test_baidu_fanyi(self, test_item):
        """百度翻译接口测试"""
        api = self.api

        # Build test_data
        test_item['fanyi.req.appid'] = app_id
        salt = random.randint(32768, 65536)
        test_item['fanyi.req.salt'] = salt
        sign = make_md5(app_id + test_item['fanyi.req.q'] + str(salt) + app_key)
        test_item['fanyi.req.sign'] = sign

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = api.payload(test_item)

        # Send request
        r = requests.post(api.url, params=payload, headers=headers)
        result = r.json()
        expected = api.load_expected(test_item)
        self.assertEqual(r.status_code, 200)
        check_result(self, expected, result) # 简单的模板验证，大家最好自己写验证。

        sleep(0.5)

    def tearDown(self):
        pass
