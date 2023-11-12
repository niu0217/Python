from pydoc import cli
from socket import *
import base64

"""
初始化信息
"""
subject = "I love computer networks!"
contenttype = "text/plain"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = "smtp.163.com"
fromAddress = 'xx@163.com'  # 发送者
toAddress = 'xx@qq.com'  # 接收者
username = base64.b64encode(fromAddress.encode()).decode()
# 这里的密码指的是邮箱的授权码
passwd = base64.b64encode('xx'.encode()).decode()

# 创建socket并和服务器取得联系
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Auth
clientSocket.send('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
    print('334 reply not received from server.')

clientSocket.send((username + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
    print('334 reply not received from server.')

clientSocket.send((passwd + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
MailFromCommand = 'MAIL FROM: <' + fromAddress + '>\r\n'
# sendall保证所有数据都被发送出去
clientSocket.sendall(MailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
RcptTo = 'RCPT TO: <' + toAddress + '>\r\n'
clientSocket.sendall(RcptTo.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
Data = 'DATA\r\n'
clientSocket.send(Data.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
Message = 'from:' + fromAddress + '\r\n'
Message += 'to:' + toAddress + '\r\n'
Message += 'subject:' + subject + '\r\n'
Message += 'Content-Type:' + contenttype + '\t\n'
Message += msg
clientSocket.sendall(Message.encode())

# Message ends with a single period.
clientSocket.sendall(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
QuitMsg = 'QUIT'
clientSocket.send(QuitMsg.encode())

clientSocket.close()

