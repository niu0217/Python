from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # (IPV4, UDP)创建套接字
serverSocket.bind(('', serverPort))  # 绑定IP地址和端口号
print('The server is ready to receive.....')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # message:客户端发来的消息 clientAddress：客户端IP和Port
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
