import mysql.connector

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
