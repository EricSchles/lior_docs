from flask import Flask, render_template,request

app = Flask(__name__, template_folder=".")

@app.route("/",methods=["GET","POST"])
def index():
	return render_template("index.html")

@app.route("/submiter",methods=["GET","POST"])
def submiter():
	name = request.form.get("name")
	return render_template("index.html",name=name)

if __name__ == '__main__':
	app.run(debug=True)
