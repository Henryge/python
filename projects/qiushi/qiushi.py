#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import urllib.request
import re
 
 
req = urllib.request.Request(url="http://www.qiushibaike.com/text/")
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req.add_header('User-Agent', user_agent)
f_obj = urllib.request.urlopen(req)
content = f_obj.read().decode("UTF-8")
# print(content)
 
# content = '''<a href="/article/119675053" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
# <div class="content">
# <span>
 
 
# 姥姥快80岁了，从我记事以来，没见她发过火，今天周六放假，我去看她，她跟安装暖气管道的工人发火了（姥姥住的老式小区，一直没有集体供暖，冬天都是去舅舅们家或者我家住），因为安装暖气管道需要从人家门前过，影响别人，（具体怎样我也不清楚）还不美观，我姥姥说啥也不安装，跟暖气工人交涉了好几次都不行，我姥姥就说，“钱退不退没关系，我不能影响别人，让别人背后戳我脊梁骨，你别给我安，你要是敢安我就砸了，我就是冻死也不愿意安，”后来我舅舅调解了一下，具体怎么办不清楚，好像得把门换了。这就是我第一次见我姥姥发脾气
# …
# </span>'''
 
pattern = re.compile('''<a href="[^\s]*" target="_blank" class="contentHerf" onclick="_hmt.push\(\['_trackEvent','web-list-content','chick'\]\)">\n<div class="content">\n<span>[\s\S]*?</span>''', re.S)
items = re.findall(pattern, content)
keystr1 = '''<a href="'''
keystr2 = '''" target="_blank"'''
keystr3 = '''<span>'''
keystr4 = '''</span>'''
for item in items:
	print(item[item.find(keystr1) + len(keystr1):item.find(keystr2)])
	print(item[item.find(keystr3) + len(keystr3):item.find(keystr4)].strip())

