from datetime import datetime
import socket
import time

server_address = ('localhost', 6789)
max_size = 4096

print("Starting the client at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	client.sendto(b'Hey!', server_address)
	time.sleep(1)
	

data, server =client.recvfrom(max_size)

print("At", datetime.now(), server, 'said', data)
client.close()
