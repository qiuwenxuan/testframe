# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: Log.py
# @Time: 2021/3/12 19:59
# @Author: sun
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from conf.config import HOME_DIR

log_file = os.path.join(HOME_DIR, "log", "log.txt")

log_format = "%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s"

log_handle = [
    logging.StreamHandler(),
    TimedRotatingFileHandler(filename=log_file, when="D", interval=1, backupCount=7)
]

logging.basicConfig(level=logging.DEBUG, handlers=log_handle, format=log_format)

LOGGER = logging.getLogger('autotest')
