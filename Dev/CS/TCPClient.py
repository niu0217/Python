from socket import *

serverName = 'localhost'  # ip地址
serverPort = 12001  # 端口号
clientSocket = socket(AF_INET, SOCK_STREAM)  # (IPV4, TCP)创建套接字

clientSocket.connect((serverName, serverPort))  # 建立TCP的三次握手

# 发送输入的消息给服务器
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())

# 接收来自服务器处理后的数据
modifiedMessage = clientSocket.recv(1024)
print(modifiedMessage.decode())

clientSocket.close()
