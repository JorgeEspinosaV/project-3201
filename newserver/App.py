from flask import Flask, render_template
from flask import request
from flask import jsonify
import psycopg2


app = Flask(__name__)

conn = psycopg2.connect(
    host="dcc.uchile.cl",
    database="cc3201",
    user="cc3201",
    password="jiPhie9aeW",
    port="321"
)
conn.autocommit = True


print("starting")

@app.route('/')
def index():
    return render_template('index.html', secure=False)



@app.route('/search')
def search():
	input = request.args.get('query')

	cur = conn.cursor()
	
	cur.execute("SELECT  nombre AS nombres, pais AS apellido_p FROM cc3201.teams LIMIT 10;")

	try:
		rows = [row for row in cur.fetchall()]
	except: 
		rows = []

	cur.close()

	return jsonify(rows)



if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)



