#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadName):
		threading.Thread.__init__(self)
		self.threadName = threadName

	def run(self):
		print(self.threadName + ":" + time.ctime(time.time()))

thread1 = myThread("thread1")
thread2 = myThread("thread2")

thread1.start()
thread2.start()

print("Main Ended")