# !/usr/bin/python
# -*- coding: UTF-8 -*-
# ---------------------------------
# @FileName: jd.py
# @Time: 2023/4/22 16:19
# @Author: sjc
# ---------------------------------
import time
from selenium.webdriver.common.by import By

from .base_page import BasicPage
from .pages.home import home_url, search_elements, result_elements


class JD(BasicPage):

    def open(self):
        self.driver.get(home_url)

    def search(self, text):
        self.input(search_elements["input"], text)
        self.click(search_elements["button"])
        time.sleep(1)

        self.scroll("down")
        time.sleep(1)

        results = []
        good_ul = self.driver.find_element(*result_elements["list"]["by"])
        good_list = good_ul.find_elements(By.TAG_NAME, "li")

        index = 0
        for each in good_list:
            name = each.find_element(*result_elements["name"]["by"]).text
            price = each.find_element(*result_elements["price"]["by"]).text

            results.append({"index": index, "name": name, "price": price})
            index += 1

        return results

    def scroll(self, direction="down"):
        if direction == "down":
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elif direction == "up":
            self.driver.execute_script("window.scrollTo(0, 0);")



