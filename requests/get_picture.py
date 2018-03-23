import requests
import os
url = "http://s0.dili360.com/www/images/magazine/logo.png"

# can't use 
# url = "http://img0.dili360.com/rw9/ga/M02/38/4B/wKgBy1VIJe6APh6lAAawz_YzRaM212.tub.jpg"
root = "/home/dean/projects/Python/requests/"
path = root + url.split('/')[-1]

try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("save successed")
	else:
		print("the file exists")
except:
	print("failed")
