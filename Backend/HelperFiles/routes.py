from flask import request, jsonify
from flask_cors import CORS 
import asyncio
from HelperFiles import flaskApp
from HelperFiles.models import User

CORS(flaskApp)

# API to create a new user
@flaskApp.route('/add_user', methods=['POST'])
def create_new_user():
    try:
        # Check if the request is empty
        if not request.data:
            return jsonify({'error': 'Request is empty'}), 400

        # Check if the JSON request contains the required fields
        required_fields = [
            'Passport_No',
            'Type',
            'Country_Code',
            'Given_Name',
            'Surname',
            'Sex',
            'Nationality',
            'Date_of_Birth',
            'Place_of_Birth',
            'Date_of_Issue',
            'Date_of_Expiration',
            'Issuing_Authority'
        ]
        data = request.json
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        user = User()  

        # Check if the Passport No. already exists in the database
        passport_no = data['Passport_No']
        existing_passports = user.get_passport_ids()
        if passport_no in existing_passports:
            return jsonify({'error': 'Passport No. already exists'}), 400

        # If all good, Add extra fields and Create user and successfull message
        data['Travel_History'] = []
        data['Face'] = "Empty" #This will Change

        user.create_user(data)
        return jsonify({'message': 'User added successfully'}), 200

    except Exception as e:
        # Handle any other exceptions that may occur
        return jsonify({'error': str(e)}), 500


# API to get all the users
@flaskApp.route('/user', methods=['GET'])
async def get_all_users():
    try:
        user = User()
        user_data = await asyncio.to_thread(user.get_user, request.args.get('id'))
        return jsonify({'users': list(user_data)})

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500