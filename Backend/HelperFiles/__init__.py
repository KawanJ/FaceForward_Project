from flask import Flask
from flask_pymongo import PyMongo

flaskApp = Flask("FF")                                                    #Creating Flask server
flaskApp.config['MONGO_URI'] = 'mongodb://localhost:27017/FaceForward_DB' #Connecting Flask Server with MongoDB Server
mongo = PyMongo(flaskApp)                                                 #Creating variable to access the MongoDB database which is connected to the Flask Server

from HelperFiles import routes