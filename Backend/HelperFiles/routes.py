from flask import request, jsonify
from flask_cors import CORS 
from HelperFiles import flaskApp
from HelperFiles.models import User

CORS(flaskApp)

@flaskApp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user = User()
    user.add_user(data)
    return jsonify({'message': 'User added successfully'})

@flaskApp.route('/view_users', methods=['GET'])
def view_users():
    user = User()
    users = user.get_users()
    return jsonify({'users': list(users)})