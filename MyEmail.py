import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qq.com"
mail_username = "869790314@qq.com"
mail_password = "djgdhiznamtnbehc"

sender = "869790314@qq.com"       #发件邮箱
receivers = ["869790314@qq.com"]  #收件邮箱

message = MIMEText("GWY邮件测试","plain","utf-8")   #内容
message['From'] = Header("869790314@qq.com", 'utf-8')   #发件人
message['To'] = Header("GWY", 'utf-8')    #收件人

message['Subject'] = Header("testing", 'utf-8')   #标题
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 465)
smtpObj.login(mail_username, mail_password)
smtpObj.sendmail(sender, receivers, message.as_string())

print("发送成功")
