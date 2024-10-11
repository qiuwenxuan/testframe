# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: base_page.py
# @Time: 2021/3/12 19:59
# @Author: sun

from selenium import webdriver


class BasicPage(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def click(self, elem):
        self.driver.find_element(*elem["by"]).click()

    def input(self, elem, value):
        e = self.driver.find_element(*elem["by"])
        e.clear()
        e.send_keys(value)

    def get_value(self, elem):
        self.driver.find_element(*elem["by"]).get_attribute(elem["get_attribute"])
