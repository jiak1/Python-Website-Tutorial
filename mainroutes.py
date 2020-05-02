from flask import render_template,Blueprint,redirect,url_for,abort
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

@routes.route('/list/<listid>')
def viewList(listid):
	if(listid is None):
		return abort()
	list = TodoList.query.filter_by(id=listid).first()
	if(list is None):
		return abort()
	return render_template("viewlist.html",todolist=list)

@routes.route('/API/addItem/<listid>/<item>')
def addItem(listid,item):
	if(listid is None or item is None):
		return abort()
	list = TodoList.query.filter_by(id=listid).first()
	if(list is None):
		return abort()
	
	newItem = TodoItem(list=list,description=item)
	db.session.add(newItem)
	db.session.commit()
	return redirect(url_for("routes.viewList",listid=listid))