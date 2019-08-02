import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.shie.com.cn"
# mail_user="gefei@shie.com.cn"
# mail_pass="Abc880915^"

sender = "gefei@shie.com.cn"
receivers = ['gefei@shie.com.cn']

message = MIMEText('您配置的URL出现超时', 'plain', 'utf-8')
message['From'] = Header("心跳应用", 'utf-8')
message['To'] = Header("gefei@shie.com.cn", 'utf-8')

subject = '超时提醒'
message['Subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	# smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("邮件发送失败")