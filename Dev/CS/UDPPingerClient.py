from socket import *
import time

serverName = '10.211.55.10'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # 设置套接字超时值1s

for i in range(0, 10):
    sendtime = time.time()  # 取得发送之前的当前时间
    message = ('Ping %d %s' % (i + 1, sendtime)).encode()  # 生成数据报，编码为bytes以便发送
    try:
        clientSocket.sendto(message, (serverName, serverPort))  # 将信息发送到服务器
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)  # 从服务器接收数据，同时也能得到服务器地址
        rtt = time.time() - sendtime  # 计算往返时间
        print('Sequence %d: Reply from %s   RTT = %.3fs' % (i + 1, serverName, rtt))
    except Exception as e:
        print('Sequence %d: Request timed out' % (i + 1))

clientSocket.close()
