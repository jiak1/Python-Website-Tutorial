from flask import Flask

app = Flask(__name__)

@app.route("/") #Create a page on the first url
def homePage():
	return "Hello World!"

app.run(host="0.0.0.0")