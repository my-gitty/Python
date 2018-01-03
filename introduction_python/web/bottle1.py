# usage:
# run bottle1.py in terminal
# then search 'http://localhost:9999' in firefox

from bottle import route, run

@route('/')
def home():
	return "It isn't fancy, but it's my home page"

run(host = 'localhost', port = 9999)

