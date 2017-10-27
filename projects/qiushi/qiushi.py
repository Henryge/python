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


pattern = re.compile('''<a href=".*?" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])"><div class="content"><span>(.*?)</span></div></a>''', re.S)
items = re.findall(pattern, content)
for item in items:
	print(item)