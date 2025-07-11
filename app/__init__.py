from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config.Config')  # Make sure the Config class is used

mongo = PyMongo(app)

from app import routes
