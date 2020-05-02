from flask import Blueprint, render_template

routes = Blueprint('routes',__name__)

@routes.route("/") #Create a page on the first url
def homePage():
	items = [
			"Cook Dinner",
			"Wash Up",
			"Do Laundry",
			"Clean Room"
	]
	return render_template("homepage.html",todolist=items)