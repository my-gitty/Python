import gevent
from gevent import socket, monkey
monkey.patch_all()

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
		 'www.baidu.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout = 5)
for job in jobs:
	print(job.value)
