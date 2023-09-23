from HelperFiles import mongo

"""
User Table:-
 - Passport_No (Primary Key)
 - Type
 - Country_Code
 - Given_Name
 - Surname
 - Sex
 - Nationality
 - Date_of_Birth
 - Place_of_Birth
 - Date_of_Issue
 - Date_of_Expiration
 - Issuing_Authority
 - Travel_History
   [
     - Airport
     - Date
     - Time
   ]
 - Face
"""

class User:
    # Method to create a new user
    def create_user(self, user_data):
        user_collection = mongo.db.users 
        user_collection.insert_one(user_data) 
    
    # Method to retrieve all users
    def get_user(self, user_id):
        user_collection = mongo.db.users
        query = {} 

        # If user_id is provided, add it to the query
        if user_id:
            query['Passport_No'] = user_id

        user_data = user_collection.find(query, {'_id': 0})
        return user_data
    
    # Method to get a list of all existing Passport IDs
    def get_passport_ids(self):
        user_collection = mongo.db.users
        passport_ids = user_collection.distinct("Passport_No")
        return passport_ids