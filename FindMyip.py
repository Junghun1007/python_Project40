
# 내부 IP 확인

import socket # 컴퓨터와 연결된 접속 정보를 받아오는 모듈

# my_addr = socket.gethostbyname(socket.gethostname()) 부정확함
# print(my_addr)

my_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_addr.connect(("www.google.co.kr", 443))
print(my_addr.getsockname()[0])

