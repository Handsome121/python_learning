import socket
import sys
#创建socket对象
ServerSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host="0.0.0.0"
port=8888
#绑定端口号
ServerSocket.bind((host,port))
#设置最大连接数，超过后排队
ServerSocket.listen(5)
while True:
    #建立客户端连接
    ClientSocket,addr=ServerSocket.accept()
    print("连接地址：%s"%str(addr))
    #从客户端接收数据
    data=ClientSocket.recv(1024)
    print('从客户端接收消息：{0}'.format(data.decode()))
    #从服务端发送数据
    msg="欢迎访问菜鸟教程"
    ClientSocket.send(msg.encode())
    ClientSocket.close()
ServerSocket.close()
#=========================================================
# TCP 服务端
# 服务端结构：
tcps = socket() #创建服务器套接字
tcps.bind()      #把地址绑定到套接字
tcps.listen()      #监听链接
while True:      #服务器无限循环
    tcpc = tcps.accept() #接受客户端链接
    while True:         #通讯循环
        tcpc.recv()/tcpc.send() #对话(接收与发送)
    tcpc.close()    #关闭客户端套接字
tcps.close()        #关闭服务器套接字(可选)

#============================================================
# TCP 客户端
# 客户端结构：
tcpc = socket()    # 创建客户端套接字
tcpc.connect()    # 尝试连接服务器
while True:        # 通讯循环
    tcpc.send()/tcpc.recv()    # 对话(发送/接收)
tcpc.close()      # 关闭客户套接字

