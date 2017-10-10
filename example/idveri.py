#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json

file = open("/home/henryge/apps/aa.txt", "r")
fo = open('/home/henryge/apps/data', 'w')

dataList = []

# while 1:
# 	line = file.readline()
# 	if  not line:
# 		break
# 	else:
# 		print line

for line in file:
	jsonText = json.loads(line)
	data = jsonText.get('userInfos')[0].get('name') + '-' + jsonText.get('userInfos')[0].get('mobile') + '-' + jsonText.get('userInfos')[0].get('certiCode') + '-' + jsonText.get('userInfos')[0].get('mobileChkRes') + '\n'
	# fo.write(data)
	dataList.append(data)
	# print data

# print dataList
fo.writelines(dataList)

file.close()
fo.close()
