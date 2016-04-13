#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename:Use requests Lib

import requests
import json

#核心一句话,get 获取一个页面及信息
def getTest(link):
    #request Lib 提供了http的所有基本请求方式，只需要一行代码
    '''
    r = request.post('http://httpbin.org/post')
    r = request.put('http://httpbin.org/put')
    r = request.delete('http://httpbin.org/delete')
    r = request.head('http://httpbin.org/head')
    r = request.options('http://httpbin.org/options')
    '''
    #函数核心就一句话
    r = requests.get(link)
    print type(r)
    print r.status_code
    print r.encoding
    #print r.text
    print r.cookies

#getTest('http://cuiqingcai.com')

#POST请求,form的数据形式
def postForm(link=''):
    payload = {'key1':'value1','key2':'value2'}
    url = 'http://httpbin.org/post'
    r = requests.post(url,data = payload)
    print r.text

#postForm()

#POST请求，json的数据格式
def postJson(Link=''):
    payload = {'key1':'value1','key2':'value2'}
    url = 'http://httpbin.org/post'
    r = requests.post(url,data = json.dumps(payload))
    print r.text

#postJson()

#POST请求，file的数据格式
def postFile(Link=''):
    files = {'file':open('test_post_file.txt','rb')}
    url = 'http://httpbin.org/post'
    r = requests.post(url,files = files)
    print r.text

#postFile()

#Cookies应用，发送cookies信息
def cookies(Link=''):
    cookies = dict(cookies_are='working')
    url = 'http://httpbin.org/cookies'
    r = requests.get(url,cookies=cookies)
    print r.text

#cookies()

'''
以下两个函数便是Session的基本用法
'''

#会话对象Session
def session(url=''):
    url = 'http://httpbin.org/cookies'
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get(url)
    print r.text

#session()

#会话对象Session
def sessionSet(url=''):
    url = 'http://httpbin.org/headers'
    s = requests.Session()
    #设置headers中的变量方法1
    s.headers.update({'x-test':'True'})
    #设置headers中的变量方法2,get会覆盖上一句的设置，设置变量为None是将其在全局配置中删除
    r = s.get(url,headers={'x-test':None})
    print r.text

#sessionSet()