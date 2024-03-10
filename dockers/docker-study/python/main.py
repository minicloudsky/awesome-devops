#!/usr/bin/env python
# coding=utf-8
import requests
import random

def get_con(url):
    response = requests.get(url)
    with open("{}.txt".format(random.randint(1,100)),'w') as f:
        f.write(response.text)
    print("url: {},status_code:{}".format(url,response.status_code))


if __name__ == '__main__':
    urls = ['https://www.baidu.com','http://www.zhihu.com']
    for url in urls:
        get_con(url)
