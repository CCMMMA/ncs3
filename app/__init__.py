import logging

from flask import Flask

from flask_httpauth import HTTPBasicAuth

from flask_cors import CORS

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the logger
log = logging.getLogger('app')

# Set the default logger level as debug
log.setLevel(logging.DEBUG)

# Create the logger formatter
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# Get the handler
h = logging.StreamHandler()

# Set the formatter
h.setFormatter(fmt)

# Add the handler to the logger
log.addHandler(h)

# Create the Flask application
app = Flask(__name__)

# Set the api enabled for cross server invocation
CORS(app)

# Configure the application from the config file
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Get the HTTP Basic Authentication object
auth = HTTPBasicAuth()

from app import routes