import socket
import sys
#创建socket对象
ClientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#与服务器建立连接
ClientSocket.connect(('127.0.0.1',8888))
#向服务器发送数据
ClientSocket.send(b"hello")
#从服务器接收数据
data=ClientSocket.recv(1024)
print('从服务端接收消息：{0}'.format(data.decode()))
#关闭套接字对象
ClientSocket.close()