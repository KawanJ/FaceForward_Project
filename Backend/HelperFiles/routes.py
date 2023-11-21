from flask import request, jsonify
from flask_cors import CORS 
import json
import asyncio
import bson
import base64
from io import BytesIO
from HelperFiles import flaskApp
from HelperFiles.models import User
from HelperFiles.recognition_module import detect_matching_face

#Cross-origin resource sharing (CORS) is required for sharing resources between multiple origins. In this case Backend <-> Frontend
CORS(flaskApp)

# Register User API

@flaskApp.route('/add_user', methods=['POST'])
def create_user(): 
    try:
        # Check if the request is empty
        if 'data' not in request.form:
            return jsonify({'error': 'Request is empty'}), 400

        # Defining the required fields
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

        # Retrieving the Data from Request
        data = json.loads(request.form['data'])

        # Check if the JSON request contains the required fields
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
            
        # Check if any field is NULL
        for k,v in data.items():
            if v == None or v == "":
                return jsonify({'error': f'Null field: {k}'}), 400
            
        if 'photo' not in request.files:
            return jsonify({'error': 'Photo missing'}), 400
        
        picbinary = bson.Binary(request.files['photo'].read())

        user = User()  

        # Check if the Passport No. already exists in the database
        passport_no = data['Passport_No']
        existing_passports = user.get_passport_ids()
        if passport_no in existing_passports:
            return jsonify({'error': 'Passport No. already exists'}), 400

        # If all good, Add extra fields and Create user and successfull message
        data['Travel_History'] = []
        data['Face'] = picbinary
        data['isVerified'] = False

        user.create_user(data)
        return jsonify({'message': 'User added successfully'}), 200

    except Exception as e:
        # Handle any other exceptions that may occur
        return jsonify({'error': str(e)}), 500


# API to get all the verified users
# The Face photo return will be in Base64 format
@flaskApp.route('/user', methods=['GET'])
async def get_user():
    try:
        user = User()
        user_data = await asyncio.to_thread(user.get_user, request.args.get('id'))
        
        # Check if Passport ID doesn't exist
        if user_data==[]:
            return jsonify({'error': 'Invalid Passport ID'}), 400
        
        # Convert BSON Object to Base64 to return as JSON
        for i in range(len(user_data)):
            user_data[i]['Face'] = base64.b64encode(user_data[i]['Face']).decode('utf-8')

        return jsonify({'users': user_data})

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500
    
# API to get all the unverified users
# The Face photo return will be in Base64 format
@flaskApp.route('/pending_requests', methods=['GET'])
async def get_unverified_user():
    try:
        user = User()
        user_data = await asyncio.to_thread(user.get_unverified_user)
        
        # Convert BSON Object to Base64 to return as JSON
        for i in range(len(user_data)):
            user_data[i]['Face'] = base64.b64encode(user_data[i]['Face']).decode('utf-8')

        return jsonify({'users': user_data})

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500
    
# The Face photo return will be in Base64 format
@flaskApp.route('/user_photo', methods=['GET'])
async def get_user_face():
    try:
        # Check if user ID is provided
        if not request.args.get('id'):
            return jsonify({'error': 'Missing Passport ID'}), 400
        
        user = User()
        user_face = await asyncio.to_thread(user.get_user_face, request.args.get('id'))
        
        # Check if Passport ID doesn't exist
        if user_face==[]:
            return jsonify({'error': 'Invalid Passport ID'}), 400
        
        # Convert BSON Object to Base64 to return as JSON
        userPhoto = base64.b64encode(user_face[0]['Face']).decode('utf-8')

        return jsonify({'Face': userPhoto})

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500
    
# API to reject and delete user regestration request based on Passport ID
@flaskApp.route('/reject_registration', methods=['DELETE'])
async def reject_user():
    try:
        passport_id = request.args.get('id')

        # Check if Passport ID is provided
        if not passport_id:
            return jsonify({'error': 'Passport ID is required for deletion.'}), 400
        
        user = User()
        result = await asyncio.to_thread(user.delete_user, passport_id)

        if result == 0:
            return jsonify({'message': 'No such User found'}), 400
        
        return jsonify({'message': 'Request Rejected successfully'}), 200

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500
    
# API to accept user regestration request based on Passport ID
@flaskApp.route('/accept_registration', methods=['POST'])
async def accept_user():
    try:
        passport_id = request.args.get('id')

        # Check if Passport ID is provided
        if not passport_id:
            return jsonify({'error': 'Passport ID is required for deletion.'}), 400
        
        user = User()
        result = await asyncio.to_thread(user.verify_user, passport_id)

        if result == 0:
            return jsonify({'message': 'No such User found'}), 400
        
        return jsonify({'message': 'Request Accepted successfully'}), 200

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500
    
# API To Verify USER for Immigration
@flaskApp.route('/verify_user', methods=['GET'])
async def user_verification():
    try:
        # Check if user ID is provided
        if not request.args.get('id'):
            return jsonify({'error': 'Missing Passport ID'}), 400
        
        user = User()
        user_face = await asyncio.to_thread(user.get_user_face, request.args.get('id'))
        
        # Check if Passport ID doesn't exist
        if user_face==[]:
            return jsonify({'error': 'Invalid Passport ID'}), 400
        
        # Convert BSON Object to Base64 to return as JSON
        userPhoto = base64.b64encode(user_face[0]['Face']).decode('utf-8')

        # Call the Verification Function
        verified = detect_matching_face(userPhoto)

        return jsonify({'status': verified})

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500
    
# API to add travel history
@flaskApp.route('/add_travel_history', methods=['POST'])
async def add_travel_history():
    try:
        data = request.get_json()
        passport_no = data["Passport_No"]
        airport = data["Airport"]
        date = data["Date"]
        time = data["Time"]

        # Check if the JSON request contains the required fields
        if not all([airport, date, time, passport_no]):
            return jsonify({"error": "Missing required fields"}), 400

        # Create the travel history entry
        travel_entry = {
            "Airport": airport,
            "Date": date,
            "Time": time
        }

        user = User()
        user_data = await asyncio.to_thread(user.get_user, passport_no)
        
        # Check if Passport ID doesn't exist
        if user_data==[]:
            return jsonify({'error': 'Invalid Passport ID'}), 400
        
        # Append the travel history entry to the user's record
        user.update_travel_history(passport_no, travel_entry)

        return jsonify({"message": "Travel history entry added successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# API to get User Travel History
@flaskApp.route('/travel_history', methods=['GET'])
async def get_travel_history():
    try:
        if request.args.get('id') == None:
            return jsonify({"Message": "Passport ID missing!"}), 400

        # Get The Results
        user = User()
        user_data = await asyncio.to_thread(user.get_travel_history, request.args.get('id'))

        # Check if Passport ID doesn't exist
        if user_data==[]:
            return jsonify({'error': 'Invalid Passport ID'}), 400
        
        return user_data

    except Exception as e:
        # Handle any exceptions that may occur
        return jsonify({'error': str(e)}), 500