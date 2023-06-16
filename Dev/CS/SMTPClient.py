from socket import *
import base64

"""
类功能：用163邮箱给qq邮箱发送消息
"""
class SendEmail:
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


if __name__ == "__main__":
	sendemail = SendEmail()
	sendemail.CreateTCPConnect()  # 和邮箱服务器建立TCP连接
	sendemail.Send_HELO()  # 发送HELO命令给邮箱服务器，测试通信是否正常
	sendemail.Send_AUTH_LOGIN()  # 给邮箱服务器发送AUTH LOGIN授权登陆
	sendemail.SendAddress()  # 给邮箱服务器发送发件人和收件人的地址
	sendemail.Send_DATA()  # 发送DATA给邮箱服务器，表示即将发送邮件内容
	sendemail.SendContent()  # 发送邮件内容
	sendemail.Send_QUIT()  # 断开和邮箱服务器的连接


