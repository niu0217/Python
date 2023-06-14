from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)  # (IPV4, TCP)创建欢迎套接字

serverSocket.bind(('', serverPort))  # 绑定IP和端口号
serverSocket.listen(1)  # 最大的连接数量至少为1
print('The server is ready to receive...')

while 1:
    # 接收来自客户端的连接，并创建一个连接套接字connectionSocket
    connectionSocket, addr = serverSocket.accept()

    # 接收来自客户端的数据，并转为大写发送给客户端
    message = connectionSocket.recv(1024)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()  # 关闭连接套接字，此时欢迎套接字并没有关闭，依旧可以处理来自客户端的连接
