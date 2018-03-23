import requests
import os
url = "http://m.ip138.com/ip.asp?ip="

r = requests.get(url+'23.3.114.83')
# print(r.status_code)
print(r.text[-308:-250])
