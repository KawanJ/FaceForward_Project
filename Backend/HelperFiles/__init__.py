from flask import Flask
from flask_pymongo import PyMongo

flaskApp = Flask("FF")
flaskApp.config['MONGO_URI'] = 'mongodb://localhost:27017/FaceForward_DB'
mongo = PyMongo(flaskApp)

from HelperFiles import routes