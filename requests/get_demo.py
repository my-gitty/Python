import requests

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup
soup =BeautifulSoup(demo, 'html.parser')


print(soup.title)
print('#'*20)

tag = soup.a
print(tag)
print('#'*20)

tag_name = soup.a.name
print(tag_name)
print('#'*20)

tag_parent_name = soup.a.parent.name
print(tag_parent_name)
print('#'*20)

tag_parent_parent_name = soup.a.parent.parent.name
print(tag_parent_parent_name)
print('#'*20)

print(tag.attrs)
print('#'*20)

print(tag.attrs['class'])
print('#'*20)

print(tag.attrs['href'])
r2 = requests.get(tag.attrs['href'])
# print(r2.text)
print('#'*20)

print(type(tag.attrs))
print('#'*20)

print(type(tag))
print('#'*20)

print(soup.a.string)
print('#'*20)


print(soup.p.string)
print('#'*20)


#####################################################
print('\n'*2)

newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")

print(newsoup.b.string)
print(type(newsoup.b.string))
print('#'*20)

print(newsoup.p.string)
print(type(newsoup.p.string))
print('#'*20)


#####################################################
print('\n'*2)


print(soup.head)
print('#'*20)

print(soup.head.contents)
print('#'*20)

print(soup.body.contents)
print('#'*20)

print(len(soup.body.contents))
print('#'*20)

print(soup.body.contents[1])
print('#'*20)

for child in soup.body.children:
	print(child)
print('#'*20)	
	
for child in soup.body.descendants:
	print(child)	
print('#'*20)
	
	
#####################################################
print('\n'*2)

print(soup.title.parent)
print('#'*20)

print(soup.html.parent)
print('#'*20)

for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)
print('#'*20)

		
#####################################################
print('\n'*2)	

print(soup.a.next_sibling)
print('#'*20)
		
print(soup.a.next_sibling.next_sibling)
print('#'*20)

print(soup.a.previous_sibling)
print('#'*20)

print(soup.a.previous_sibling.previous_sibling)
print('#'*20)

print(soup.a.parent)
print('#'*20)

for sibling in soup.a.next_siblings:
	print(sibling)	
print('#'*20)
	
for sibling in soup.a.previous_siblings:
	print(sibling)
print('#'*20)

#####################################################
print('\n'*2)

print(soup.prettify()) 
print('#'*20)

print(soup.a.prettify())
print('#'*20)





























