#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("/home/henryge/apps/test.txt", "w")
print "文件名为: ", fo.name
seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
fo.writelines( seq )

# 关闭文件
fo.close()