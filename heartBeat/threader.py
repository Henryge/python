from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import os,time,random

def task(n):
	print("%s is running" % os.getpid())
	return n**2

if __name__ == "__main__":
	executor = ProcessPoolExecutor(max_workers=11)
	futures = []
	for i in range(11):
		future = executor.submit(task, i)
		futures.append(future)
	executor.shutdown(True)
	print("+++>")
	for future in futures:
		print(future.result())