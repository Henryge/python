#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib.request
import re
import os

INDEX_ = 'http://www.xuanshu.com/soft/sort02/index_'

webroot = 'http://www.xuanshu.com'

for page in range(20,220):
    print('正在下载第'+str(page)+'页小说')

    url = INDEX_ + str(page) + '.html'
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  }
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request,timeout=180)


    html = response.read().decode('utf-8')
    pattern = re.compile(u'<li>.*?<div class="s">.*?target="_blank">(.*?)</a><br />大小：(.*?)<br>.*?</em><br>更新：(.*?)</div>.*?<a href="(.*?)"><img.*?>(.*?)</a>.*?<div class="u">(.*?)</div>',re.S)
    items = re.findall(pattern,html)
    #print items

    for item in items:
        # try:
            book_auther = item[0]
            book_size = item[1]
            book_updatetime = item[2]
            book_link = item[3]
            book_name = item[4]
            book_note = item[5]

            book_full_link = webroot + book_link    # 构建书的绝对地址

            #请求地址
            request = urllib.request.Request(book_full_link,headers=headers)
            response = urllib.request.urlopen(request,timeout=180)

            html = response.read().decode('utf-8')
            #print html
            pattern = re.compile('<a class="downButton.*?<a class="downButton" href=\'(.*?)\'.*?Txt.*?</a>',re.S)
            down_link = re.findall(pattern,html)
            print(book_name)
            print(down_link)

            # down txt
            request = urllib.request.Request(down_link[0],headers=headers)
            response = urllib.request.urlopen(request,timeout=180)
            fp = open(book_name+'.txt','w')

            print('start download')
            fp.write(response.read())
            print('down finish\n')
            fp.close()
        # except Exception,e:
        #     print '该条目解析出现错误，忽略'
        #     print e
        #     print ''
        #     fp = open('error.log','a')
        #     fp.write('page:'+str(page)+'\n')
        #     fp.write(item[4].encode('gbk'))
        #     #fp.write(e)
        #     fp.write('\nThere is an error in parsing process.\n\n')
        #     fp.close()