from socket import *
from select import select

# 创建监听套接字，作为初始监控对象
sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)
# 设置为非阻塞
sockfd.setblocking(False)
#设置关注列表
rlist=[sockfd]
wlist=[]
xlist=[]
#循环监控关注的IO
while True:
    rs,ws,xs=select(rlist,wlist,xlist)#返回值为准备就绪的IO
    #遍历就绪的读IO列表，分情况讨论，监听套接字和客户端连接套接字
    for r in rs:
        if r is sockfd:
            conn,addr=r.accept()
            print("connect from",addr)
            # 客户端连接套接字也设置为非阻塞
            conn.setblocking(False)
            # 将连接进来的客户端连接套接字加入到关注的读IO中
            rlist.append(conn)
        else:
            #某个客户端发送了消息
            data=r.recv(1024).decode()
            # 客户端断开或结束
            if not data:
                #操作系统取消关注
                rlist.remove(r)
                #客户端连接套接字关闭
                r.close()
                #for循环继续遍历后面的IO
                continue #跳过后面继续执行下一次
            #打印收到的数据
            print(data)
            #如果服务端要向客户端发送消息，则将客户端连接套接字加入到写IO中
            wlist.append(r)
        #遍历写IO列表
        for w in ws:
            #服务端向客户端发送消息这件事也被关注
            w.send(b"ok")
            #发送完一个消息就从写IO列表中移除，不然每当客户端发送过来消息服务端就主送发送消息给客户端，
            # 因为上一条发过来消息时建立的连接套接字已经加入到了写IO中，每次收发消息行为上是独立的
            wlist.remove(r)

