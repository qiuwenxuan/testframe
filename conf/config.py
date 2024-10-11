# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: config.py
# @Time: 2021/3/12 19:59
# @Author: sun
import os
from configparser import ConfigParser

_conf_dir = os.path.dirname(__file__)
_conf_file = os.path.join(_conf_dir, 'config.ini')


class MyParser(ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d


def _get_all_conf():
    _config = MyParser()
    result = {}
    if os.path.isfile(_conf_file):
        try:
            _config.read(_conf_file, encoding='UTF-8')
            result = _config.as_dict()
        except OSError:
            raise ValueError("Read config file failed: %s" % OSError)
    return result


config = _get_all_conf()
sys_cfg = config['sys']
log_cfg = config['log']
smtp_cfg = config['smtp']
email_cfg = config['email']

HOME_DIR = os.path.dirname(os.path.dirname(__file__))
CASE_DIR = os.path.join(HOME_DIR, "testcase")
REPORT_DIR = os.path.join(HOME_DIR, "report")
