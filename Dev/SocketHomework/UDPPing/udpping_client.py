from email import message
import random
from socket import *
import time

serverName = '127.0.0.1'
serverPort = 12000
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

RTTList = []
RTTMin = float(1)
RTTMax = float(0)

for i in range(10):
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
        # Otherwise, the server responds
    try:
        oldTime = time.time()  # 返回当前时间的时间戳
        # 格式化时间
        sendTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(oldTime))
        message = 'package %d, client local time:%s' % (i + 1, sendTime)

        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - oldTime
        RTTList.append(rtt)
        RTTMax = max(rtt, RTTMax)
        RTTMin = min(rtt, RTTMin)
        print("Ping %d %s RTT:%f" % (i + 1, modifiedMessage.decode(), rtt))

    except Exception as e:
        print('Request timed out')

print("\n>> Summary: RTT Min: %f, RTT Max %f, RTT Mean: %f" % (RTTMin, RTTMax, sum(RTTList) / len(RTTList)))
