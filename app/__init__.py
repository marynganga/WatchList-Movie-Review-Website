from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

# Creating Flask Extensions Instances
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
	# initialize application
	app = Flask(__name__)

	# setting up configuration
	app.config.from_object(config_options[config_name])

	# initializing flask extensions
	bootstrap.init_app(app)
	dp.init_app(app)

	# registering the blueprint
	from .main import main as main_blueprint

	app.register_blueprint(main_blueprint)

	# setting config
	from .request import configure_request
	configure_request(app)

	return app