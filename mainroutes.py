from flask import render_template,Blueprint,redirect,url_for,abort,jsonify
from models import TodoList,TodoItem
from program import db

routes = Blueprint('routes', __name__)

@routes.route('/register')
def register():
	return render_template('register.html')

@routes.route('/login')
def login():
	return render_template('login.html')

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

@routes.route('/API/editItem/<itemID>/<newValue>')
def editItem(itemID,newValue):
	if(itemID is None or newValue is None):
		return jsonify(success=False)
	item = TodoItem.query.filter_by(id=itemID).first()
	if(item is None):
		return jsonify(success=False)
	#Item exists and we are ready to change
	item.description = newValue
	db.session.commit()
	return jsonify(success=True)