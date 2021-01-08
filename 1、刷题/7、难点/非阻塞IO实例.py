from socket import *
import time

log = open("my.log", "a")
# 创建TCP套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)
# 设置为非阻塞
sockfd.setblocking(False)
# 设置超时时间3S
sockfd.settimeout(3)
while True:
    try:
        print("waiting for connect")
        conn, addr = sockfd.accept()
        print("connect from", addr)
    except BlockingIOError as e:
        # 做一些和accept无关的IO事情
        msg = "%s:%s\n" % (time.ctime(), e)
        log.write(msg)
        log.flush()
        time.sleep(2)
    except timeout as e:
        # 做一些和accept无关的IO事情
        msg = "%s:%s\n" % (time.ctime(), e)
        log.write(msg)
        log.flush()
        time.sleep(2)
    else:
        # 有客户端连接
        data=conn.recv(1024)
        print(data.decode())

