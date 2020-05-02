from program import db

class TodoList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable=False,default="My Todo List")
	items = db.relationship('todo_item',backref='list',lazy='dynamic')

class TodoItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	listID = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
	description = db.Column(db.String(100),nullable=False,default="")