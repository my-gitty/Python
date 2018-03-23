import requests

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "ERROR"


if __name__ == "__main__":
	url = "http://item.jd.com/2967929.html"
	# print(getHTMLText(url))
	
	
	# use the key word to search
	keyword = {'wd':'Python'}
	url1 = "http://www.baidu.com/s?"
	r = requests.get(url1, params = keyword)
	print(len(r.text))
