#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__= 'Mr.Ming'

import urllib
import urllib2
import re

#百度贴吧抓取帖子
#面向对象编程

#处理页面标签类
class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

class BDTB(object):

    #初始化传入帖子的地址，是否只看楼主的参数
    def __init__(self,baseURL,seeLZ):
        self.baseURL=baseURL
        self.seeLZ='?see_lz='+str(seeLZ)   #网址see_lz为小写，更正
        self.tool = Tool()
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            #print response.read().decode('utf-8')
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print '连接百度贴吧失败，错误原因',e.reason
                return None
    #获取帖子的标题
    def getTitle(self):
        page=self.getPage(1)
        pattern = re.compile('<h3 class ="core_title_txt.*?">(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1) # test print ontent
            return result.group(1).strip()
        else:
            return None
    #获取帖子的总页数
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)#test print
            return result.group(1).strip()
        else:
            return None

    #获取正文内容
    def getContent(self,page):
        #print page    #test page content
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        #for item in items:
        #    print item
        print self.tool.replace(items[3])

baseURL= 'http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL,1)
bdtb.getContent(bdtb.getPage(1))




























