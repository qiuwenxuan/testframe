# !/usr/bin/python
# -*- coding: UTF-8 -*-
# ---------------------------------
# @FileName: screen.py
# @Time: 2023/4/22 19:32
# @Author: sjc
# ---------------------------------
import os
import time

from PIL import ImageGrab
from conf.config import HOME_DIR

screen_home = os.path.join(HOME_DIR, "log", 'Screen')


def screen(name):
    t = time.time()
    png = ImageGrab.grab()

    _today = time.strftime("%Y%m%d")
    screen_path = os.path.join(HOME_DIR, "log", 'Screen', _today)
    if not os.path.exists(screen_path):
        os.makedirs(screen_path)
    image_name = os.path.join(screen_path, name)
    png.save('%s_%s.png' % (image_name, str(round(t * 1000))))
