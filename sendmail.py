#coding:utf-8
import smtplib
from email.mime.text import MIMEText
_user = "9077****@qq.com"
_pwd  = "tkjftoa****"
#qq邮箱外部调用需要手动开启IMAP/SMTP服务，获得授权码，而不是普通的账户密码登录
_to   = "9077****@qq.com"

msg = MIMEText("手机有货了快去买啊！")
msg["Subject"] = "手机有货了快去买买买啊！"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e
#crontab -e
#30 12 16 2 * /home/sendmail.py
