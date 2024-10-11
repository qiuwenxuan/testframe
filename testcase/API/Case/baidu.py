# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @FileName: baidu.py
# @Time: 2021/3/13 9:16
# @Author: sun


import requests
import random
import json
from hashlib import md5
from Comm.data import read_excel

# Set your own appid/appkey.
app_id = '20210313000725421'
app_key = 'ro3HGgrEp7V1_EfvXdQe'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'en'
to_lang = 'zh'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

query = 'Hello World! This is 1st paragraph.\n' + \
        'This is 2nd paragraph.'


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


salt = random.randint(32768, 65536)
sign = make_md5(app_id + query + str(salt) + app_key)

# Build request
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'appid': app_id, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

# Send request
r = requests.post(url, params=payload, headers=headers)
result = r.json()
print(result)

# Show response
print(json.dumps(result, indent=4, ensure_ascii=False))