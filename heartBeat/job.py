class HBJob(object):
	def __init__(self, id, url, appName, beatSeconds, noticeEmails, noticeCount,noticeTimes,isDeleted):
		self.id = id
		self.url = url
		self.appName = appName
		self.beatSeconds = beatSeconds
		self.noticeEmails = noticeEmails
		self.noticeCount = noticeCount
		self.noticeTimes = noticeTimes
		self.isDeleted = isDeleted

	def toString(self):
		return str(self.id) + "|" + self.url + "|" + self.appName + "|" + str(self.beatSeconds) + "|" + self.noticeEmails + "|" + str(self.noticeCount) + "|" + str(self.noticeTimes) + "|" + self.isDeleted