"""
select io多路复用方法 示例
"""
from select import select
from socket import *

# 搞几个IO 用于监控
tcp_socket = socket()
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

file = open('my.log','a')

print("对IO进行监控")
rs,ws,xs = select([udp_socket,file],[udp_socket,file],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)