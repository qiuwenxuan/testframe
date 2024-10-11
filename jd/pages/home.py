# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

home_url = 'https://www.jd.com'


search_elements = {
    "input": {'by': (By.ID, 'key'), "get_attribute": "text"},
    "button": {'by': (By.CLASS_NAME, u'button'), "get_attribute": None}
}

result_elements = {
    "list": {'by': (By.XPATH, ".//div[@id='J_goodsList']/ul"), "get_attribute": None},
    "price": {'by': (By.XPATH, ".//div[@class='p-price']/strong/i"), "get_attribute": "text"},
    "name": {'by': (By.XPATH, ".//div[@class='p-name p-name-type-2']/a/em"), "get_attribute": "text"}
}
