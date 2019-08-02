import mysql.connector,time

class HBDB(object):
	def __init__(self):
		self.mydb = mysql.connector.connect(
			host='172.20.8.130',
			user='iprs_dev',
			passwd='iprs_dev',
			#auth_plugin='mysql_native_password'
			database='iprs_dev01'
		)

	def getAllJobs(self):
		mycursor = self.mydb.cursor()
		mycursor.execute("select id, url, app_name, beat_seconds, notice_emails, notice_count, notice_times, is_deleted from t_hb_jobs")
		myresult = mycursor.fetchall()
		return myresult

	def saveHist(self, jobId):
		mycursor = self.mydb.cursor()
		sql = "insert into t_hb_hist(job_id, time_out_time, is_notice, job_time) values (%s,%s,%s,%s)"
		val = (jobId, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'Y', time.strftime('%Y-%m-%d', time.localtime()))
		print(val)
		mycursor.execute(sql, val)
		self.mydb.commit()

	def getNoticeTimes(self, jobId, localtime):
		mycursor = self.mydb.cursor()
		mycursor.execute("select count(1) from t_hb_hist where job_id = " + str(jobId) + " and job_time = '" + localtime + "' and is_notice = 'Y'")
		myresult = mycursor.fetchall()
		return myresult
