import time,mysql.connector
from apscheduler.schedulers.blocking import BlockingScheduler
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from db import HBDB
from hbCache import HBCache
from job import HBJob

def job():
	jobs = HBDB().getAllJobs()
	hbCache = HBCache()
	for x in jobs:
		cacheJob = hbCache.getJobById(x[0])
		if len(cacheJob) == 0:
			hbCache.putJob(HBJob(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
		else:
			jobStr = str(x[0]) + "|" + str(x[1]) + "|" + str(x[2]) + "|" + str(x[3]) + "|" + str(x[4]) + "|" + str(x[5]) + "|" + str(x[6]) + "|" + str(x[7])
			if cacheJob[0] != jobStr:
				print(str(x[0]) + "出现修改:" + jobStr)
	#启动相应的线程组
	exeJobs = hbCache.getJobs()
	executor = ProcessPoolExecutor(max_workers=len(exeJobs))
	futures = []
	for exeJob in exeJobs:
		future = executor.submit(ping, exeJob)
		futures.append(future)
	executor.shutdown(True)

def ping(job):
	print(job.beatSeconds)
	time.sleep(job.beatSeconds)
	code = os.system("ping -n 1 -w 1 www.baidu.com")
	if code:
		print("ping is fail")
	else:
		print("ping is ok")

if __name__=='__main__':
	scheduler = BlockingScheduler()

	scheduler.add_job(job, 'interval', seconds=3)

	scheduler.start()