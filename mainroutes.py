from flask import render_template,Blueprint,redirect,url_for
from models import TodoList,TodoItem
from program import db

routes = Blueprint('routes', __name__)

@routes.route('/lists')
def showLists():
	lists = TodoList.query.all()
	return render_template("showlists.html",todolists=lists)

@routes.route("/addlist")
def addList():
	newList = TodoList()
	newList.name = "New Todo List"
	db.session.add(newList)
	db.session.commit()
	return redirect(url_for('routes.showLists'))

@routes.route('/')
def index():
	items = [
		"Cook Dinner",
		"Wash Up",
		"Do Laundry",
		"Clean Room"
	]
	return render_template("homepage.html",todolist=items)