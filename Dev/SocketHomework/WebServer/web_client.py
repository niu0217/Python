from socket import *
import sys  # In order to terminate the program


clientSocket = socket(AF_INET, SOCK_STREAM)
ServerPort = 6789
ServerName = '127.0.0.1'
clientSocket.connect((ServerName, ServerPort))

# 给服务器发送消息
Head = ("GET /HelloWorld.html HTTP/1.1\r\n"
        "Host: %s:%s\r\n"
        "Connection: close\r\n"
        "User-agent: Mozilla/5.0\r\n"
        "Accept-language: en") % (ServerName, ServerPort)
clientSocket.send(Head.encode('utf-8'))

# 打印收到的消息
while True:
    data = clientSocket.recv(1024)
    if len(data) == 0:
        break
    print(data.decode())
    with open('response.html', 'ab+') as f:
        f.write(data)
