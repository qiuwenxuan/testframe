# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: data.py
# @Time: 2021/3/12 19:59
# @Author: sun
import pandas as pd


def read_excel(file, **kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file, **kwargs)
        print(data)
        data_dict = data.to_dict('records')
    finally:
        print(data_dict)
        return data_dict

