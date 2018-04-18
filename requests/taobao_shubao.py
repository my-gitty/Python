import requests
from bs4 import BeautifulSoup
import re
import time


def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ilt, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		# print(plt)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price, title])
	except:
		print("")



def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("Number", "Price", "Goods"))
	count = 0
	
	for lt in ilt:
		count = count + 1
		print( tplt.format(count, lt[0], lt[1]))


def main():
	goods = r'书包'
	depth = 5
	time_ps = time.strftime('%Y%m%d', time.localtime(time.time()))
	
	start_url = r'https://s.taobao.com/search?q=' + goods + r'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_' + str(time) + r'ie=utf8&'
	infoList = []
	for i in range(depth):
		try:
			url = start_url + r'bcoffset=' + str(-i*3) + r'&ntoffset=' + str(-i*3) + r'&p4ppushleft=1%2C48&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
			
	printGoodsList(infoList)
	
main()
