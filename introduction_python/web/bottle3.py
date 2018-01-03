# usage:
# run bottle3.py in terminal, and the 'index.html' should exit
# then search 'http://localhost:9999' in firefox

from bottle import route, run, static_file

@route('/')
def home():
	return static_file('index.html', root = '.')

@route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s!" % thing

run(host = 'localhost', port = 9999)
