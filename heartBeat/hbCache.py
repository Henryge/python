import os

class HBCache(object):
	def __init__(self):
		cacheFile = os.open("jobsCache.txt", os.O_RDONLY|os.O_CREAT)
		os.close(cacheFile)

	def putJob(self, job):
		print("添加新的JOB：" + job.toString())
		cacheFile = open("jobsCache.txt", "a")
		cacheFile.write(job.toString())
		cacheFile.write("\n")
		cacheFile.close()

	def getJobs(self):
		cacheFile = open("jobsCache.txt", "r")
		jobs = cacheFile.readlines()
		cacheFile.close()
		return jobs

	def updateJobs(self, index, job):
		cacheFile = open("jobsCache.txt", "r")
		jobs = cacheFile.readlines()
		cacheFile.close()
		resultJobs = []
		for job in jobs:
			position = job.index("|")
			if job[:position] == id:
				resultJobs.append(job)
		return resultJobs;

	def getJobById(self, id):
		cacheFile = open("jobsCache.txt", "r")
		jobs = cacheFile.readlines()
		cacheFile.close()
		resultJobs = []
		for job in jobs:
			job = job.strip("\n")
			print(job)
			if job.strip("\n") != "":
				position = job.index("|")
				if job[:position] == str(id):
					resultJobs.append(job)
			else:
				print("job为空")
		return resultJobs;
