# !/usr/bin/python
# -*- coding: UTF-8 -*-
# ---------------------------------
# @FileName: test_jd.py
# @Time: 2023/4/22 17:16
# @Author: sjc
# ---------------------------------
import ddt
from unittest import TestCase

from jd.jd import JD

test_data = [
    ("电脑", 60),
    ("显示器", 59)
]


@ddt.ddt  # 数据驱动 DDT
class TestJD(TestCase):

    @ddt.data(*test_data)   # 数据驱动 DDT
    def test_search(self, test_item):
        """京东搜索测试"""
        key = test_item[0]
        count = test_item[1]
        d = JD()
        d.open()
        r = d.search(key)
        print(r)

        self.assertEqual(len(r), count)
