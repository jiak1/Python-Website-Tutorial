from program import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class TodoList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable=False,default="My Todo List")
	items = db.relationship('TodoItem',backref='list',lazy='dynamic')
	ownerID = db.Column(db.Integer,db.ForeignKey('account.id'))
	
class TodoItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	listID = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
	description = db.Column(db.String(100),nullable=False,default="")

class Account(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100),nullable=False)
	email = db.Column(db.String(120),nullable=False)
	password_hash = db.Column(db.String(128),nullable=True)

	lists = db.relationship('TodoList',backref='Owner',lazy='dynamic')

	def set_password(self,password):
		self.password_hash = generate_password_hash(password)
	
	def check_password(self,password):
		if(self.password_hash != None):
			return check_password_hash(self.password_hash,password)
		else:
			return False