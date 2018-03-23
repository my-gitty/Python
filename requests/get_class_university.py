import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def fillUnivList(ulist, html):
	import bs4
	soup =BeautifulSoup(html, 'html.parser')
	for tr in soup.find('tbody').children:
		# print(tr)
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td') # ???
			print(tds)
			ulist.append([tds[0].string.encode('utf-8'), tds[1].string.encode('utf-8'), tds[3].string.encode('utf-8')])

def printUnivList(ulist, num):
	print("{:^10}\t{:^6}\t\t\t{:^10}".format("Grade", "School", "Score"))
	for i in range(num):
		u = ulist[i]
		print("{:^10}\t{:^6}\t\t\t{:^10}".format(u[0], u[1], u[2]))
	
	
def main():
	uinfo = []
	url =  'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 50)
	
main()


