import socket

# 实例化一个用户数据报对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 本机的ip
r_addr = '10.2.243.218', 1026
# 指定端口号
# 绑定 ip 和端口号
s.bind(r_addr)

# 指定要发送数据的 ip 和端口号
s_addr = '10.2.85.132', 1025
# 向指定的 ip 和端口号发送数据
s.sendto('hello'.encode('utf-8'), s_addr)

s.close()