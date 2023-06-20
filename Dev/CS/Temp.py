from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

"""
函数功能：用163邮箱给qq邮箱发送消息（使用SMTP)
"""
def SendEmailSMTP():
    mail_server = 'smtp.163.com'
    port = 25

    sender = '19502357024@163.com'  # 发送者的邮箱账号
    sender_pass = 'POXRVKCPYHUXITXA'  # 发送者的SMTP授权码
    receiver = '2335658505@qq.com'  # 接收方的邮箱账号

    # 构建给接收方的消息，特别要注意格式
    mail_msg = 'this is a test'  # 写给发送者的内容
    msg = MIMEText(mail_msg, 'plain', 'utf-8')
    msg['From'] = sender  # 发送人
    msg['To'] = receiver  # 接收人
    msg['Subject'] = Header('testone', 'utf-8')  # 标题

    try:
        mail = SMTP(mail_server, port)  # 创建SMTP对象
        mail.login(sender, sender_pass)  # 授权（发送方邮箱账号，发送方的SMTP授权码）
        mail.sendmail(sender, receiver, msg.as_string())  # 利用SMTP对象发送消息
        mail.quit()  # 断开和SMTP服务器的连接
        print("邮件发送成功！")
    except:
        mail.quit()
        print("邮件发送失败！")
