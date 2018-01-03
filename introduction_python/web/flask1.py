# usage:
# run flask1.py in terminal, and the 'index.html' should exit
# then search 'http://localhost:9999' in firefox
# then search 'http://localhost:9999/echo/Mothra' in firefox

from flask import Flask

app = Flask(__name__, static_folder = '.', static_url_path = '')

@app.route('/')
def home():
	return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s!" % thing

app.run(port = 9999, debug = True)
