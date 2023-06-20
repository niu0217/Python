from socket import *
import base64

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


"""
类功能：用163邮箱给qq邮箱发送消息（使用socket)
"""
class SendEmailSocket:
	def __init__(self):
		self.HOST = 'smtp.163.com'
		self.PORT = 25
		self.BUFSIZE = 1024
		self.ADDR = (self.HOST, self.PORT)
		self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
		self.user = base64.b64encode(b'*****').decode() + '\r\n'  # *****是发送账户
		self.passward = base64.b64encode(b'*****').decode() + '\r\n'  # ****是发送账户的授权码

	"""
	函数功能：和邮箱服务器建立TCP连接
	"""
	def CreateTCPConnect(self):
		self.tcpCliSock.connect(self.ADDR)
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print(recv)
		if recv[:3] != b'220':
			print('220 reply not received from server.')

	"""
	函数功能：发送HELO命令给邮箱服务器，测试通信是否正常
	"""
	def Send_HELO(self):
		helloCommand = 'HELO niu0217\r\n'
		self.tcpCliSock.send(helloCommand.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('hello:', recv)
		if recv[:3] != b'250':
			print('250 reply not received from server.')

	"""
	函数功能：给邮箱服务器发送AUTH LOGIN授权登陆
	"""
	def Send_AUTH_LOGIN(self):
		login = 'AUTH LOGIN\r\n'
		self.tcpCliSock.send(login.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('login:', recv)

		self.tcpCliSock.send(self.user.encode())  # 用户名
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('user:', recv)

		self.tcpCliSock.send(self.passward.encode())  # 密码
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('password:', recv)

	"""
	函数功能：给邮箱服务器发送发件人和收件人的地址
	"""
	def SendAddress(self):
		mailFrom = 'MAIL FROM: <*****>\r\n'  # *****是发送方账号
		self.tcpCliSock.send(mailFrom.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('mail from: ', recv)

		rcptTo = 'RCPT TO: <*****>\r\n'  # *****是接收方账号
		self.tcpCliSock.send(rcptTo.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('rcpt: ', recv)

	"""
	函数功能：发送DATA给邮箱服务器，表示即将发送邮件内容
	"""
	def Send_DATA(self):
		data = 'DATA\r\n'
		self.tcpCliSock.send(data.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('data: ', recv)

	"""
	函数功能：发送邮件内容
	"""
	def SendContent(self):
		from_ = '*****'  # *****是发送方账号
		to = '*****'  # *****是接收方账号
		headers = [
			'From: %s' % from_,
			'To: %s' % to,
			'Subject: sen SMTP',
		]

		body = [
			'Hello',
			'World',
		]
		msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))
		print(msg.encode())
		self.tcpCliSock.send(msg.encode())
		endmsg = '\r\n.\r\n'
		self.tcpCliSock.send(endmsg.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('msg: ', recv)

	"""
	函数功能：断开和邮箱服务器的连接
	"""
	def Send_QUIT(self):
		byebye = 'QUIT\r\n'
		self.tcpCliSock.send(byebye.encode())
		recv = self.tcpCliSock.recv(self.BUFSIZE)
		print('quit: ', recv)

		self.tcpCliSock.close()


"""
类功能：用163邮箱给qq邮箱发送消息（使用SMTP)
"""
class SendEmailSMTP:
	def __init__(self):
		self.mail_server = 'smtp.163.com'
		self.port = 25
		self.sender = '19502357024@163.com'  # 发送者的邮箱账号
		self.sender_passward = 'POXRVKCPYHUXITXA'  # 发送者的SMTP授权码
		self.receiver = '2335658505@qq.com'  # 接收方的邮箱账号

	"""
	函数功能：构建发送消息
	"""
	def BuildContent(self, messageFormat):
		if messageFormat == 'text':  # 发送文本
			mail_msg = 'I am a text!!'
			msg = MIMEText(mail_msg, 'plain', 'utf-8')
		elif messageFormat == 'html':  # 发送html
			mail_msg = """
			<p>Python 邮件发送测试...</p>
			<p><a href="http://www.runoob.com">这是一个链接</a></p>
			"""
			msg = MIMEText(mail_msg, 'html', 'utf-8')
		elif messageFormat == 'attach':  # 发送附件
			msg = MIMEMultipart()
			msg.attach(MIMEText('测试发送附件', 'plain', 'utf-8'))  # 正文内容

			# 发送附件1
			# attach1 = MIMEText(open('test.txt', 'r').read(), 'base64', 'utf-8')
			attach1 = MIMEApplication(open('test.txt', 'rb').read(), 'base64')
			attach1['Content-Type'] = 'applocation/octet-stream'
			attach1['Content-Disposition'] = 'attachment; filename="test.txt"'
			msg.attach(attach1)

			# 发送附件2
			attach2 = MIMEApplication(open('runboo.xlsx', 'rb').read(), 'base64')
			attach2['Content-Type'] = 'applocation/octet-stream'
			attach2['Content-Disposition'] = 'attachment; filename="runboo.xlsx"'
			msg.attach(attach2)

		elif messageFormat == 'image':
			msg = MIMEMultipart()
			msg.attach(MIMEText('测试发送图片', 'plain', 'utf-8'))  # 正文内容

			mail_msg = """
			<p>Python 邮件发送测试...</p>
			<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
			<p>图片演示：</p>
			<p><img decoding="async" src="cid:image1"></p>
			"""
			msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

			attach1 = MIMEImage(open('test.png', 'rb').read())
			attach1.add_header('Content-ID', '<image1>')
			msg.attach(attach1)
		else:
			pass
		msg['From'] = self.sender
		msg['To'] = self.receiver
		msg['Subject'] = Header('niu0217', 'utf-8')

		return msg

	"""
	函数功能：发送邮件
	"""
	def SendMessage(self):
		try:
			mail = SMTP(self.mail_server, self.port)  # 创建SMTP对象
			mail.login(self.sender, self.sender_passward)  # 授权（发送方邮箱账号，发送方的SMTP授权码）
			# msg = self.BuildContent('text')  # 构建发送消息(文本)
			# msg = self.BuildContent('html')  # 构建发送消息(html)
			# msg = self.BuildContent('attach')  # 构建发送消息(附件)
			msg = self.BuildContent('image')  # 构建发送消息(图片)
			mail.sendmail(self.sender, self.receiver, msg.as_string())  # 利用SMTP对象发送消息
			mail.quit()  # 断开和SMTP服务器的连接
			print('邮件发送成功')
		except:
			mail.quit()
			print('邮件发送失败')


if __name__ == "__main__":
	"""
	测试用例：测试SendEmail
	"""
	# sendemail = SendEmailSocket()
	# sendemail.CreateTCPConnect()  # 和邮箱服务器建立TCP连接
	# sendemail.Send_HELO()  # 发送HELO命令给邮箱服务器，测试通信是否正常
	# sendemail.Send_AUTH_LOGIN()  # 给邮箱服务器发送AUTH LOGIN授权登陆
	# sendemail.SendAddress()  # 给邮箱服务器发送发件人和收件人的地址
	# sendemail.Send_DATA()  # 发送DATA给邮箱服务器，表示即将发送邮件内容
	# sendemail.SendContent()  # 发送邮件内容
	# sendemail.Send_QUIT()  # 断开和邮箱服务器的连接

	"""
	测试用例：测试SendEmailSMTP
	"""
	sendmail = SendEmailSMTP()
	sendmail.SendMessage()




