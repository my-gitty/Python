def get_links(url):
	import requests
	from bs4 import BeautifulSoup as soup
	result = requests.get(url)
	page = result.text
	doc = soup(page)
	
	# the 'a' express a link of the HTML and the 'herf' express a address of the link.
	links = [ element.get('href') for element in doc.find_all('a')]
	return links

if __name__ == '__main__':
	import sys
	try:
		if sys.argv[1]:
			for url	in sys.argv[1:]:
				print('Links in ', url)
				for num, link in enumerate(get_links(url), start = 1):
					print(num, link)
				print()
	except:
		print('No have enough paraters!')
		print('The usage:')
		print('python beautifulsoup.py http://boingboing.net')
