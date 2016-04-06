#!/user/bin/python
# -*- coding: utf-8 -*-

import os
import re
import urllib
import time

#显示下载进度
def schedule(a,b,c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    #reg=r'src="(.+?\.jpeg)"'
    reg=r'class="BDE_Image".*?src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist=re.findall(imgre,html)
    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+\
        "-"+str(t.__getattribute__("tm_mday"))+"-"+str(t.__getattribute__("tm_hour"))+\
        "."+str(t.__getattribute__("tm_min"))
    picpath = 'D:\\ENVS\\python\\workspace\\parse\\getpic\\%s' %(foldername)

    if not os.path.exists(picpath):
        os.makedirs(picpath)
    x=0
    for imgurl in imglist:
        target = picpath+'\\%s.jpg'%x
        print 'Downloading image to location:'+target+'\url='+imgurl
        image=urllib.urlretrieve(imgurl,target,schedule)
        x+=1
        time.sleep(0.5)
    return image


if __name__=='__main__':
    print '''             *************************************
             **      Welcome to use Spider     **
             **     Created on  2016-04-6      **
             **       @author: Mr Ming         **
             *************************************'''
    # html= getHtml("http://tieba.baidu.com/p/2460150866")                 #使用更详细正则匹配，筛选需要的图片 re+ " pic_ext'
    #html= getHtml("http://www.zngirls.com/g/18214/")                     #无法下载图片，防盗链设置，注意：src=‘’
    #html= getHtml("http://360.mafengwo.cn/travels/info.php?id=3237101")  #注意问题2，img格式为jpeg
    html= getHtml("http://tieba.baidu.com/p/4453707129?pn=2")

    getImg(html)
    print 'Download has finished.'