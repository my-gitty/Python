# usage:
# run flask3c.py in terminal, and the 'flask3.html' should exit
# then search 'http://localhost:9999/echo/?thing=Gorgo&place=Wilmerding' in firefox

from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
	kwargs = {}
	kwargs['thing'] = request.args.get('thing')
	kwargs['place'] = request.args.get('place')
	return render_template('flask3.html', **kwargs)

app.run(port = 9999, debug = True)
