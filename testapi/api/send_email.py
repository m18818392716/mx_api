import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from testapi.api.get_conf import get_conf

def send_email(text):
    today = time.strftime('%Y.%m.%d',time.localtime(time.time()))
    sender, receiver, smtpserver, username, password = get_conf()
    # subject为邮件主题 text为邮件正文
    subject = "[api_test]接口自动化测试结果通知 {}".format(today)
    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = "".join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()