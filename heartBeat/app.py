import time,mysql.connector,os,smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from db import HBDB
from hbCache import HBCache
from job import HBJob
from email.mime.text import MIMEText
from email.header import Header

def ping(job):
	code = os.system("ping -n 1 -w 1 " + job.url)
	if code:
		count = HBDB().getNoticeTimes(job.id, time.strftime('%Y-%m-%d', time.localtime()))
		print("该JOB当天已经通知：" + str(count[0][0]) + "次,限制为:" + str(job.noticeTimes) + "次")
		if count[0][0] < job.noticeTimes:
			HBDB().saveHist(job.id)
			email(job)
	else:
		print("ping is ok")

def email(job):
	mail_host="smtp.shie.com.cn"

	sender = "gefei@shie.com.cn"
	receivers = job.noticeEmails.split(",")

	message = MIMEText('您配置的URL出现超时: ' + job.url, 'plain', 'utf-8')
	message['From'] = Header("心跳应用", 'utf-8')
	message['To'] = Header("用户", 'utf-8')

	subject = '超时提醒'
	message['Subject'] = Header(subject, 'utf-8')

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)
		smtpObj.sendmail(sender, receivers, message.as_string())
	except smtplib.SMTPException:
		print("邮件发送失败")

	# jobs = HBDB().getAllJobs()
	# hbCache = HBCache()
	# exeJobs = []
	# for x in jobs:
		# cacheJob = hbCache.getJobById(x[0])
		# if len(cacheJob) == 0:
		# 	hbCache.putJob(HBJob(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
		# exeJobs.append(HBJob(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
		# else:
		# 	jobStr = str(x[0]) + "|" + str(x[1]) + "|" + str(x[2]) + "|" + str(x[3]) + "|" + str(x[4]) + "|" + str(x[5]) + "|" + str(x[6]) + "|" + str(x[7])
		# 	if cacheJob[0] != jobStr:
				# print(str(x[0]) + "出现修改:" + jobStr)
	#启动相应的线程组
	# exeJobs = hbCache.getJobs()
	# executor = ProcessPoolExecutor(max_workers=len(exeJobs))
	# futures = []
	# for exeJob in exeJobs:
	# 	future = executor.submit(ping, exeJob)
	# 	futures.append(future)
	# executor.shutdown(True)

# def ping(job):
# 	print(job.url)
# 	start = time.time()
# 	while True:
# 		end = time.time()
# 		if end - start >= 3:
# 			break
# 		time.sleep(job.beatSeconds)
# 		code = os.system("ping -n 1 -w 1 " + job.url)
# 		if code:
# 			print("ping is fail")
# 		else:
# 			print("ping is ok")

if __name__=='__main__':
	scheduler = BlockingScheduler()

	jobs = HBDB().getAllJobs()
	exeJobs = []
	for x in jobs:
		exeJobs.append(HBJob(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))

	for exeJob in exeJobs:
		print(exeJob.url)
		scheduler.add_job(ping, 'interval', seconds=exeJob.beatSeconds, args=[exeJob])

	scheduler.start()