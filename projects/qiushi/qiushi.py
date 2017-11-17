#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import re

def openURL(inputURL):
	req = urllib.request.Request(inputURL)
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	req.add_header('User-Agent', user_agent)
	f_obj = urllib.request.urlopen(req)
	return f_obj.read().decode("UTF-8")

# req = urllib.request.Request(url="http://www.qiushibaike.com/text/")
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# req.add_header('User-Agent', user_agent)
# f_obj = urllib.request.urlopen(req)
# content = f_obj.read().decode("UTF-8")
# print(content)

content = openURL("http://www.qiushibaike.com/text/")

pattern = re.compile('''<a href="[^\s]*" target="_blank" class="contentHerf" onclick="_hmt.push\(\['_trackEvent','web-list-content','chick'\]\)">\n<div class="content">\n<span>[\s\S]*?</span>''', re.S)
items = re.findall(pattern, content)
keystr1 = '''<a href="'''
keystr2 = '''" target="_blank"'''
keystr3 = '''<span>'''
keystr4 = '''</span>'''
for item in items:
	content = openURL('http://www.qiushibaike.com' + item[item.find(keystr1) + len(keystr1):item.find(keystr2)])
	pattern = re.compile('''<div class="content">[\s\S]*?</div>''', re.S)
	texts = re.findall(pattern, content)
	for text in texts:
		print(text)

	# print('http://www.qiushibaike.com' + item[item.find(keystr1) + len(keystr1):item.find(keystr2)])
	# print(item[item.find(keystr3) + len(keystr3):item.find(keystr4)].strip())



