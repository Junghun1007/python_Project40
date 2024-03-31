
# 외부 IP 주소
import requests
import re
req_addr = requests.get("http://ipconfig.kr")
my_out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req_addr.text)[1]
print(my_out_addr)