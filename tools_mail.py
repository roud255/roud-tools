import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
邮件发送
'''


#传图片的绝对路径
def sendMail(img):
    # 发送邮件相关参数
    smtpserver = 'smtp.163.com'#这里用的是网易163邮箱
    port = 465
    #发送者邮箱
    sender = ''
    #授权码token
    psw = ''
    #接受者邮箱
    receiver = ""
    #主题
    subjext = ''
    message = MIMEMultipart()
    message['from'] = sender
    message['to'] = receiver
    message['subject'] = subjext
    #邮箱内容
    text = 'roud工具'
    text_plain = MIMEText(text,'plain','utf-8') #正文转码
    message.attach(text_plain)
    SendImageFile = open(img,'rb').read()
    image = MIMEImage(SendImageFile)
    image['Content-Disposition'] = 'attachment;filename="img.jpg"'
    message.attach(image)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, message.as_string())
    os.remove(img)
    smtp.quit()