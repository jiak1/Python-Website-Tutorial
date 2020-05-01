from flask import Flask,render_template

app = Flask(__name__)
#
@app.route("/") #Create a page on the first url
def homePage():
	return render_template("homepage.html")
	
app.run(host="0.0.0.0")