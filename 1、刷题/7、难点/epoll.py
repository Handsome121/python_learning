"""
基于 empoll 方法的IO多路复用并发模型
"""
from socket import *
from select import *

# 创建监听套接字,作为初始监控对象
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(5)

# 设置为非阻塞
sockfd.setblocking(False)

# poll对象
p = select.empoll()

# 查找字典 {fileno:sockfd} 与关注的IO保持一致
map = {sockfd.fileno(): sockfd}
# 关注监听套接字
p.register(sockfd, EMPOLLIN)

# 循环监控关注的IO
while True:
    events = p.poll() # events->[(1,2)]
    # 遍历就绪的IO列表,分情况讨论 监听套接字和客户端连接套接字
    for fd, event in events:
        if fd == sockfd.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 将链接进来的客户端链接套接字加入关注
            connfd.setblocking(False)
            p.register(connfd, EMPOLLIN)
            # 字典也要维护
            map[connfd.fileno()] = connfd
        elif event == EMPOLLIN:
            # 某个客户端发送了消息
            data = map[fd].recv(1024).decode()
            if not data:
                # 客户端结束
                p.unregister(fd)  # 取消关注
                map[fd].close()
                del map[fd] # 从字典中移除
                continue  # for循环继续遍历后面的IO
            print(data)
            # map[fd].send(b'OK')
            p.register(fd,EMPOLLOUT)
        elif event == EMPOLLOUT:
            map[fd].send(b'OK')
            p.register(fd, EMPOLLIN)

