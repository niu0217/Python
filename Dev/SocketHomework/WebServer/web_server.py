from socket import *
# 实现多线程需要导入的包
import threading


def webProcess(connectionSocket):
    """
    函数功能：线程回调函数，处理连接的客户
    """
    try:
        # 接收客户端发送来的消息
        message = connectionSocket.recv(1024).decode('utf-8')
        print(message)
        filename = message.split()[1]
        f = open(filename[1:], encoding='utf-8')
        outputdata = f.read()
        # Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(header.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        # 发送消息结束标志
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        ErrorMessage = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(ErrorMessage.encode())
        # Close client socket
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=webProcess, args=(connectionSocket,))
    # thread start to run
    thread.start()
    thread.join()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
