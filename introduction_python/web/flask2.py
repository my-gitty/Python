# usage:
# run flask2.py in terminal, and the 'flask2.html' should exit
# then search 'http://localhost:9999/echo/Gamera' in firefox

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
	return render_template('flask2.html', thing = thing)

app.run(port = 9999, debug = True)
