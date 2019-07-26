import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

if __name__=='__main__':
	scheduler = BlockingScheduler()

	scheduler.add_job(job, 'interval', seconds=2)

	scheduler.start()