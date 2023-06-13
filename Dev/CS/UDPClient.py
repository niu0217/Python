from socket import *

# serverName = '10.211.55.10'
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # (IPV4, UDP)创建套接字

messgae = input('Input lowercase sentence:')  # 输入要发送给服务器的消息
clientSocket.sendto(messgae.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # modifiedMessage:服务器返回的消息  serverAddress：服务器的地址
print(modifiedMessage.decode())
clientSocket.close()  # 关闭套接字

