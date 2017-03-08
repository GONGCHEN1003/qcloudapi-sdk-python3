#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base

class Wenzhi(Base):
    #requestHost = '183.60.118.226'
    #requestHost = 'cvm.api.qcloud.com'
    requestHost = 'wenzhi.api.qcloud.com'

def main():
    action = 'DataSearch'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {
        "content" : "123",
    }
    service = Wenzhi(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()
