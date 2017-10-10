#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import urllib

fo = open('D:\\Person.txt', 'w')

data = urllib.urlopen("http://www.baidu.com/").read()

fo.write(data)

fo.close()

