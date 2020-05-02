from flask import render_template,Blueprint
from models import TodoList,TodoItem

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/index')
def index():
	items = [
		"Cook Dinner",
		"Wash Up",
		"Do Laundry",
		"Clean Room"
	]
	return render_template("homepage.html",todolist=items)