from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
	app = Flask(__name__, static_url_path="", static_folder="static")

	with app.app_context():
		from mainroutes import routes
		app.register_blueprint(routes)

		return app
		