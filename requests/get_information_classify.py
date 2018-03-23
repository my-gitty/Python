import requests

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup
soup =BeautifulSoup(demo, 'html.parser')

print('#'*20)
for link in soup.find_all('a'):
	print(link.get('href'))
print('#'*20)

	
for tag in soup.find_all(True):
	print(tag.name)	
print('#'*20)

import re
for tag in soup.find_all(re.compile('b')):
	print(tag.name)
print('#'*20)

print(soup.find_all('p', 'course'))
print('#'*20)

print(soup.find_all(id = 'link1'))
print('#'*20)

print(soup.find_all(id = re.compile('link')))
print('#'*20)

print(soup.find_all(id = 'link'))
print('#'*20)

print(soup.find_all('a', recursive = False))
print('#'*20)

print(soup.find_all(string = 'Basic Python'))
print('#'*20)

print(soup.find_all(string = re.compile('python')))
print('#'*20)
