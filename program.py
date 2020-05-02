from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
	app = Flask(__name__,static_url_path="", static_folder="static")
	app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://jackdbusername:dbpassword@remotemysql.com/jackflaskproject"
	
	
	db.init_app(app)
	
	with app.app_context():
		from mainroutes import routes
		app.register_blueprint(routes)

		db.create_all()
		return app