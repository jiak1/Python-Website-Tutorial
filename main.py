from flask import Flask,render_template

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/") #Create a page on the first url
def homePage():
	items = [
		"Cook Dinner",
		"Wash Up",
		"Do Laundry",
		"Clean Room"
	]
	return render_template("homepage.html",todolist=items)
	
app.run(host="0.0.0.0")