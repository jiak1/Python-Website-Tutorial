from flask import render_template,Blueprint,redirect,url_for,abort,jsonify,flash
from models import TodoList,TodoItem,Account
from program import db,login
from flask_login import current_user, login_user
from forms import RegisterForm,LoginForm

routes = Blueprint('routes', __name__)

@login.user_loader
def load_account(id):
	return Account.query.get(int(id))

@routes.route('/register',methods=['GET','POST'])
def register():
	if(current_user.is_authenticated):
		return redirect(url_for('routes.showLists'))
	form = RegisterForm()
	if(form.validate_on_submit()):
		#someone is trying to register an account
		user = Account(username = form.username.data,email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("Successfully created your Account!","success")
		return redirect(url_for('routes.login'))
	else:
		for problem in form.errors:
			flash(form.errors[problem][0],"danger")
	return render_template('register.html',form=form)

@routes.route('/login',methods=['GET','POST'])
def login():
	if(current_user.is_authenticated):
		return redirect(url_for('routes.showLists'))
	form = LoginForm()
	if(form.validate_on_submit()):
		user = Account.query.filter_by(username=form.username.data).first()
		if(user is None or not user.check_password(form.password.data)):
			flash("Invalid username or password","danger")
			return redirect(url_for('routes.login'))
		login_user(user,remember=True)
		return redirect(url_for('routes.showLists'))
	else:
		for problem in form.errors:
			flash(form.errors[problem][0],"danger")

	return render_template('login.html',form=form)

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