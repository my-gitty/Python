# usage:
# run flask3a.py in terminal, and the 'flask3.html' should exit
# then search 'http://localhost:9999/echo/Rodan/McKeesport' in firefox

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
	return render_template('flask3.html', thing = thing, place = place)

app.run(port = 9999, debug = True)
