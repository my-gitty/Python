import requests

r = requests.get('http://www.baidu.com')

# if status_code = 200, the results is successed
# 404 is not successed
print(r.status_code)


r.encoding = 'utf-8'

# from the contents to analyse the encoding of web
# r.apparent_encoding

# HTTP's reponse in binary
# print(r.content)

# print contents
# print(r.text)


print(type(r))

print(r.headers)



