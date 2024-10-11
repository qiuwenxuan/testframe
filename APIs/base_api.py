# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: base_api.py
# @Time: 2021/3/13 11:30
# @Author: sun
import logging
import random
import importlib
import copy
import json
import unittest
from hashlib import md5
from ipaddress import ip_address
from Comm.compare import json_compare


logger = logging.getLogger('main.api')
req_prefix = 'req.'
res_prefix = 'res.'


def _separate_data(data, prefix='req.'):
    pfx = prefix
    result = {}
    for key, value in data.items():
        if key.startswith(pfx):
            req_key = key[len(pfx):]
            result[req_key] = value
    return result


def _get_cmd(key, dict_name='payload'):
    separator = '.'
    cmd = dict_name
    if separator in key:
        data_key = key.split(separator)
        for each in data_key:
            if each.isdigit():
                cmd = cmd + '[' + each + ']'
            else:
                cmd = cmd + '[\'' + each + '\']'
        cmd = cmd + ' = value'
    else:
        cmd = cmd + '[key] = value'
    return cmd


def check_result(unittest_testcase, x, y):
    # 只有x,y完全相同才能通过，任意不同则返回失败。建议自己在用例中做结果检查
    testcase = unittest_testcase
    diff = json_compare(x, y)
    testcase.assertEqual(x, y)


class BaseAPI(object):
    def __init__(self, api):
        self.api = api
        self.api_name = None
        self.url = ''
        self.req_template = {}
        self.res_template = {}
        self._get_api_param()

    def _get_api_param(self):
        """动态加载API定义文件，获取文件中定义的API参数"""
        try:
            m = importlib.import_module(self.api)
            self.api_name = m.API_NAME
            self.url = m.url
            self.req_template = m.req_param
            self.res_template = m.res_param
        except Exception as e:
            logger.error('error info : %s' % e)

    def payload(self, data=None):
        payload = copy.deepcopy(self.req_template)
        if data:
            req_pre = '.'.join([self.api_name, req_prefix])
            req_data = _separate_data(data, req_pre)
            for key, value in req_data.items():
                cmd = _get_cmd(key, 'payload')
                exec(cmd)
        return payload

    def load_expected(self, data=None):
        expected = copy.deepcopy(self.res_template)
        if data:
            res_pre = '.'.join([self.api_name, res_prefix])
            res_data = _separate_data(data, res_pre)
            for key, value in res_data.items():
                cmd = _get_cmd(key, 'expected')
                exec(cmd)
        return expected


def get_random_headers():
    rip = ip_address('0.0.0.0')
    hds = [{'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92/iPhone 8 Plus'},
           {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F72/iPhone 6s'},
           {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79/iPhone 6'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.0.0; zh-cn; RNE-AL00 Build/HUAWEIRNE-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; RNE-AL00 Build/HUAWEIRNE-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; OPPO R11 Build/NMF26X) Apple WebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; VIVO Y85A Build/OPM1.171019.011) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.3.0; zh-cn; RNE-AL00 Build/HUAWEIRNE-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBAM00 Build/OPM1.171019.026) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; MI 8 Build/PKQ1.180729.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'},
           {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.3.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.365 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3'}]
    while rip.is_private:
        rip = ip_address('.'.join(map(str, (random.randint(0, 255) for _ in range(4)))))
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9',
               'pragma': 'no-cache',
               'cache-control': 'no-cache',
               'upgrade-insecure-requests': '1',
               'user-agent': hds[random.randint(0, len(hds) - 1)]['User-Agent'],
               'X-Real-IP': str(rip),
               'X-Forwarded-For': str(rip)}
    return headers
