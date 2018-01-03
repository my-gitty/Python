import urllib.request as ur

url = 'https://www.baidu.com/'
conn = ur.urlopen(url)
print(conn)

data = conn.read()
print('read data:')
print(data)

print('\nconnect status:')
print(conn.status)

print('\nContent-Type:')
print(conn.getheader('Content-Type'))

print('\nconnect getheaders:')
for key, value in conn.getheaders():
	print(key, '\t', value)
