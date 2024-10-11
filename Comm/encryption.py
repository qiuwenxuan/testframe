# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: encryption.py
# @Time: 2021/3/14 10:26
# @Author: sun
from hashlib import md5


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
