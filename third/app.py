from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__, template_folder=".")

def insert_into_db(name):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("insert into names (name) values (?)" [name])
		con.commit()

def select_all_from_db():
	with sql.connect("database.db") as con:
		cur = con.cursor()
		vals = cur.execute("select * from names").fetchall()	
	return vals

@app.route("/",methods=["GET","POST"])
def index():
	return render_template("index.html")

@app.route("/iwanttosubmit", methods=["GET","POST"])
def iwanttosubmit():
	my_name = request.form.get("name")
	insert_into_db(my_name)
	return render_template("index.html")

@app.route("/showvals",methods=["GET","POST"])
def showvals():
	vals = select_all_from_db()
	values = []
	for val in vals:
		values.append(str(val))
	return render_template("index.html",vals=values)

if __name__ == '__main__':
	app.run(debug=True)