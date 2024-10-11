# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: compare.py
# @Time: 2021/3/14 10:49
# @Author: sun
import json_tools


def json_compare(x, y):
    diff = json_tools.diff(x, y)
    if diff:
        for action in diff:
            if 'add' in action:
                print('++增加元素:', action['add'], ' 值:', action['value'])
            elif 'remove' in action:
                print('--删除元素:', action['remove'], ' 值:',  action['prev'])
            elif 'replace' in action:
                print('**修改元素:', action['replace'], ' 值:', action['prev'], '-->', action['value'])
    return diff
