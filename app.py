import os

from flask import Flask  # etc.
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

# Create and name Flask app
app = Flask("FlaskLoginApp")

# database connection
app.config['MONGODB_SETTINGS'] = {'db': 'flask-login'}
app.config['SECRET_KEY'] = 'dhfdrhrd'
app.debug = os.environ.get('DEBUG', False)

db = MongoEngine(app)  # connect MongoEngine with Flask App
app.session_interface = MongoEngineSessionInterface(db)  # sessions w/ mongoengine

# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)
