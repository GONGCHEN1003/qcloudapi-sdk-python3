#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'wenzhi'
action = 'LexicalAnalysis'
config = {
    'Region': 'sh',
    'secretId': '你的id',
    'secretKey': '你的sec',
    'method': 'post'
}
params = {
    'text': '这是新api第一次测试，尝试通过新api接入npl',
    'code': 2097152
}
try:
    service = QcloudApi(module, config)
    print(service.generateUrl(action, params))
    print(service.call(action, params))
    #service.setRequestMethod('get')
    #print service.call('DescribeCdnEntities', {})
except Exception as e:
    print(e)
