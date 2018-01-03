# usage:
# run bottle2.py in terminal, and the 'index.html' should exit
# then search 'http://localhost:9999' in firefox

from bottle import route, run, static_file

@route('/')
def home():
	return static_file('index.html', root = '.')

run(host = 'localhost', port = 9999)
